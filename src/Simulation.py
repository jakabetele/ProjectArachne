import numpy as np
import pandas as pd
import math
import random
import time

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

import imageio
from io import BytesIO

import os

#from src.FoodNet import FoodNet
from src.Map import Map
from src.Animal import Animal

class Simulation():

    def __init__(self,
                 map_: Map,
                 foodnet: dict,
                 species_all: dict,
                 list_of_animals_all : list[Animal],
                 simulation_config_obj: dict):

        
        self.map_ = map_
        self.map_size = [self.map_.size_x, self.map_.size_y]

        self.foodnet = foodnet

        self.species_all = species_all

        self.list_of_animals_all = list_of_animals_all

        self.run_type = simulation_config_obj['run_type']
        if self.run_type == 'limited':
            self.simulation_steps = simulation_config_obj['simulation_steps']
        elif self.run_type == 'endless':
            self.min_species = simulation_config_obj['min_species']

        self.print_info = simulation_config_obj['print_info']
            
        self.generate_simulation_gif = simulation_config_obj['generate_simulation_gif']
        if self.generate_simulation_gif:
            self.frame_duration = simulation_config_obj['frame_duration']
            self.save_path = simulation_config_obj['save_path']
            self.plot_config_obj = simulation_config_obj['plot_config_obj']

        self.begin = 0
        self.end = 0

        self.map_state_all = []
        self.animal_state_all = []
        self.interaction_pos_all = []
        self.interaction_map = [[[] for j in range(self.map_.size_y)] for i in range(self.map_.size_x)]
    
    def print_time_info(self, func):
        if self.print_info:
            self.end = time.time()
            print(f"\tTime: {round(self.end  - self.begin, 2)} -> {func}")
            self.begin = time.time()
        else:
            pass

    def draw_field_background(self, ax, df_map_state):

        height = self.map_size[0]
        width = self.map_size[1]

        image_data = np.zeros((height, width, 4), dtype=float)

        rgba_colors = mcolors.to_rgba_array(df_map_state['color'])
        rgba_colors[:, 3] = df_map_state['alpha']
        image_data[df_map_state['y'], df_map_state['x']] = rgba_colors
        ax.imshow(image_data, origin='lower')

        ax.set_xlim(-0.5, width - 0.5)
        ax.set_ylim(-0.5, height - 0.5)
        ax.set_aspect('equal')
        
    def generate_gif(self):
        x_size = self.map_.size_x
        x_tolr = int(x_size * 0.01)
        y_size = self.map_.size_y
        y_tolr = int(y_size * 0.01)

        sim_len = len(self.animal_state_all)
        sim_len_tol = int(sim_len * 0.01)

        max_animal = max([df_animal_state['species'].value_counts()[0] for df_animal_state in self.animal_state_all if df_animal_state.shape[0] != 0])
        max_animal_tol = int(max_animal * 0.01)

        history_all = []

        with imageio.get_writer(self.save_path + "simulation.gif", mode='I', duration = 0.33) as writer:

            for i, (df_animal_state, df_map_state) in enumerate(zip(self.animal_state_all, self.map_state_all)):
                if self.print_info:
                    print(f"_________________________BEGIN OF STATE {i} RENDER_________________________")
                    self.begin = time.time()
                
                fig, ax = plt.subplots(2, 1, figsize = (10, 12), gridspec_kw={'height_ratios': [3, 1]})
                fig.tight_layout()

                species_all = df_animal_state['species'].unique()

                for species in species_all:
                    nr_animal = df_animal_state[df_animal_state['species'] == species].shape[0]
                    species_color = df_animal_state['color'][df_animal_state['species'] == species].iloc[0]
                    history_all.append([species, i, nr_animal, species_color])

                df_history = pd.DataFrame(history_all, columns=['species', 'step', 'nr_animal', 'color'])

            
                # Top plot
                ax[0].grid(True)
                ax[0].set_xlim(left=0 - x_tolr, right=x_size + x_tolr)
                ax[0].set_ylim(bottom=0 - y_tolr, top=y_size + y_tolr)

                self.draw_field_background(ax[0], df_map_state)
                self.print_time_info("draw_field_background()")

                ax[0].scatter(x=df_animal_state['x'], y=df_animal_state['y'], color=df_animal_state['color'])
                self.print_time_info("ax[0].scatter()")

                # Bottom plot
                ax[1].grid(True)
                ax[1].set_xlim(left=0 - sim_len_tol, right=sim_len + sim_len_tol)
                ax[1].set_ylim(bottom=0, top=max_animal + max_animal_tol)

                for species in df_history['species'].unique():

                    df_species = df_history[df_history['species'] == species]
                    color_species = df_species['color'].iloc[0]
                    label_v = df_species['nr_animal'].iloc[-1]
                    if df_species.shape[0] < i:
                        label_v = 0

                    ax[1].plot(df_species['step'], df_species['nr_animal'], color=color_species, label = f"{species}: {label_v}")
                ax[1].legend(loc = 'upper left')
                self.print_time_info("ax[1].scatter()")

                buf = BytesIO()
                plt.savefig(buf, format='png')
                ax[0].clear()
                ax[1].clear()
                #plt.close(fig)
                buf.seek(0)

                image = imageio.v3.imread(buf, extension='.png')
                writer.append_data(image)
                buf.close()
                self.print_time_info("writer.append_data(image)")

                if self.print_info:
                    print(f"//////////////////////////END OF STATE {i} RENDER//////////////////////////")
                    print()
    
    def build_interaction_map(self):
        self.interaction_pos_all = []

        for animal in self.list_of_animals_all:
            animal.move()
            pos = animal.get_pos()

            if len(self.interaction_map[pos[0]][pos[1]]) == 0:
                self.interaction_pos_all.append(pos)

            self.interaction_map[pos[0]][pos[1]].append(animal)

        return True

    def animal_interaction(self, animal_a: Animal, animal_b: Animal):
        if animal_a == animal_b:
            return False

        if animal_b.species in self.foodnet[animal_a.species]: # animal_b is a pray animal of animal_a
                animal_a.hunt(animal_b)
        elif animal_a.species in self.foodnet[animal_b.species]: # animal_a is a pray animal of animal_b
                animal_b.hunt(animal_a)
        else:
            pass

        return True

    def simulate_interactions_pos(self, animals_interact_pos: list[Animal]):
        nr_animals = len(animals_interact_pos)
        random.shuffle(animals_interact_pos)

        for i in range(0, nr_animals-1):
            animal_a = animals_interact_pos[i]
            
            if animal_a.alive:
                for j in range(i+1, nr_animals):
                    animal_b = animals_interact_pos[j]
                    
                    if animal_b.alive:
                        self.animal_interaction(animal_a, animal_b)
                    else:
                        pass
            else:
                pass
        
        return True

    def generate_interaction_zone(self, pos, range_):
        x, y = pos
        size_x, size_y = self.map_size

        x_min = max(0, int(math.floor(x - range_)))
        x_max = min(size_x - 1, int(math.ceil(x + range_)))
        y_min = max(0, int(math.floor(y - range_)))
        y_max = min(size_y - 1, int(math.ceil(y + range_)))

        zone = [
            [(i, j), math.hypot(i - x, j - y)]
            for i in range(x_min, x_max + 1)
            for j in range(y_min, y_max + 1)
            if math.hypot(i - x, j - y) <= range_
        ]
        zone.sort(key=lambda item: item[1])
        zone = [coord for coord, _ in zone]

        return zone

    def simulate_interactions(self):
        nr_animals = len(self.list_of_animals_all)
        random.shuffle(self.list_of_animals_all)
        
        for i in range(nr_animals - 1, -1, -1):
            animal = self.list_of_animals_all[i]
            
            if animal.is_alive():
                pos = animal.get_pos()
                feed_range = animal.get_feed_range()
                interaction_zone = self.generate_interaction_zone(pos, feed_range)

                for pos in interaction_zone:
                    if len(self.interaction_map[pos[0]][pos[1]]) != 0:
                        for animal_b in self.interaction_map[pos[0]][pos[1]]:
                            self.animal_interaction(animal, animal_b)

            else:
                del animal
                self.list_of_animals_all.pop(i)
    
    def feed_from_ground(self):
        alive_animals = [animal for animal in self.list_of_animals_all if animal.alive]

        if not alive_animals:
            return

        positions = np.array([animal.get_pos() for animal in alive_animals], dtype=np.int32)
        x_coords, y_coords = positions[:, 0], positions[:, 1]
        
        cell_nutritions = self.map_.nutrition_grid[y_coords, x_coords]
        cell_type_indices = self.map_.type_grid[y_coords, x_coords]
        
        consumed_amounts = np.zeros(len(alive_animals))

        for i, animal in enumerate(alive_animals):
            cell_type_name = self.map_.type_names[cell_type_indices[i]]

            if cell_type_name in self.foodnet[animal.species]:
                consumed = animal.eat_field(cell_nutritions[i])
                consumed_amounts[i] = consumed
            
        ate_indices = np.where(consumed_amounts > 0)[0]
        ate_x, ate_y = x_coords[ate_indices], y_coords[ate_indices]
        
        np.subtract.at(self.map_.nutrition_grid, (ate_y, ate_x), consumed_amounts[ate_indices])

        self.list_of_animals_all = alive_animals

    def append_animal_state(self, step):
        state = []
        nr_animal = len(self.list_of_animals_all)
        for i in range(nr_animal-1, -1, -1):
            animal = self.list_of_animals_all[i]
            
            if animal.alive:
                pos = animal.get_pos()
                species  = animal.get_species()
                color = animal.get_color()
                state.append([species, color, pos[0], pos[1]])
            else:
                del animal
                self.list_of_animals_all.pop(i)
        
        df_animal_state = pd.DataFrame(state, columns = ['species', 'color', 'x', 'y'])
        df_animal_state['step'] = step
        self.animal_state_all.append(df_animal_state)
    
    def append_map_state(self, step):
        df_map_state = self.map_.get_state()
        df_map_state['step'] = step

        self.map_state_all.append(df_map_state)

    def end_of_step(self):
        new_born_all = []
        nr_animal = len(self.list_of_animals_all)
        
        for i in range(nr_animal-1, -1, -1):
            animal = self.list_of_animals_all[i]
            animal.get_older()

            if animal.is_alive():

                if animal.gender == 'Female':
                    nr_offsprings = animal.bread()
                    pos = animal.get_pos()

                    for j in range(nr_offsprings):
                        offspring = Animal(self.map_size, self.species_all[animal.species])
                        offspring.position = pos
                        new_born_all.append(offspring)
                
            else:
                del animal
                self.list_of_animals_all.pop(i)
        
        self.list_of_animals_all += new_born_all

    def clear_interaction_map(self):
        for pos in self.interaction_pos_all:
                self.interaction_map[pos[0]][pos[1]] = []

    def start_limited(self):
        self.append_animal_state(0)
        self.append_map_state(0)

        for i in range(1, self.simulation_steps + 1):
            if self.print_info:
                    print(f"_________________________BEGIN OF STEP {i}_________________________")
                    self.begin = time.time()

            self.build_interaction_map()
            self.print_time_info("build_interaction_map()")

            self.simulate_interactions()
            self.print_time_info( "simulate_interactions()")

            self.feed_from_ground()
            self.print_time_info("feed_from_ground()")

            self.map_.regenerate_grass()
            self.print_time_info("map_.regenerate_grass()")
            
            self.end_of_step()
            self.print_time_info("end_of_step()")
            
            self.clear_interaction_map()
            self.print_time_info("clear_interaction_map()")
            
            self.append_animal_state(i)
            self.print_time_info("append_animal_state()")

            self.append_map_state(i)
            self.print_time_info("append_map_state()")

            if self.print_info:
                if len(self.list_of_animals_all) == 0:
                    print(f"//////////////////////////GLOBAL EXTINSION AT STEP {i}//////////////////////////")
                    break
                else: 
                    print(f"//////////////////////////END OF STEP {i}//////////////////////////")
                    print()

    def start_endless(self):
        self.append_animal_state(0)
        self.append_map_state(0)

        i = 0
        while self.animal_state_all[-1]['species'].value_counts().shape[0] >= self.min_species:
            i+=1
            if self.print_info:
                    print(f"_________________________BEGIN OF STEP {i}_________________________")
                    self.begin = time.time()

            self.build_interaction_map()
            self.print_time_info("build_interaction_map()")

            self.simulate_interactions()
            self.print_time_info( "simulate_interactions()")

            self.feed_from_ground()
            self.print_time_info("feed_from_ground()")

            self.map_.regenerate_grass()
            self.print_time_info("map_.regenerate_grass()")
            
            self.end_of_step()
            self.print_time_info("end_of_step()")
            
            self.clear_interaction_map()
            self.print_time_info("clear_interaction_map()")
            
            self.append_animal_state(i)
            self.print_time_info("append_animal_state()")

            self.append_map_state(i)
            self.print_time_info("append_map_state()")

            if self.print_info:
                if len(self.list_of_animals_all) == 0:
                    print(f"///////////////////////////GLOBAL EXTINSION AT STEP {i}///////////////////////////")
                    break
                else: 
                    print(f"///////////////////////////END OF STEP {i}///////////////////////////")
                    print()
        
        self.append_animal_state(i+1)
        self.append_map_state(i+1)
        print(self.animal_state_all[-1]['species'].value_counts())

    def start(self):

        if self.run_type == 'limited':
            self.start_limited()
        elif self.run_type == 'endless':
            self.start_endless()
        
        if self.generate_simulation_gif:
            self.generate_gif()
        
        return self.animal_state_all, self.map_state_all

    def __del__(self):
        return True
