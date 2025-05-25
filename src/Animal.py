import numpy as np

import random

import math

import warnings
warnings.filterwarnings("ignore")

class Animal(object):

    def __init__(self, map_size: [int], config_obj : dict):
        
        self.map_size = map_size
        
        self.species = config_obj["species"]
        self.color = config_obj["color"]

        self.energy = config_obj["initial_energy"]
        self.nutrition_value = config_obj["nutrition_value"]
        self.feed_range = config_obj["feed_range"]

        self.life_expectancy = config_obj["life_expectancy"]
        self.maturity = config_obj["maturity"]
        self.fertility = config_obj["fertility"]
        self.min_energy_to_bread = config_obj["min_energy_to_bread"]
        self.breading_cost_per_offspring = config_obj["breading_cost_per_offspring"]

        self.mobility = config_obj["mobility"]
        self.unit_energy_consumption = config_obj["unit_energy_consumption"]
        
        self.fight_stat = config_obj["fight_stat"]
        self.fight_costs = config_obj["fight_costs"]
        
        self.alive = True
        self.age = 0
        self.death_time = self.generate_random_gaussian(self.life_expectancy[0], self.life_expectancy[1])
        self.gender = random.choice(['Male', 'Female'])
        self.position = [int(random.random() * (map_size[0] - 1)),
                         int(random.random() * (map_size[1] - 1))]

    def generate_random_gaussian(self, mean: float, std: float):
        return random.gauss(mean, std**2)
    
    def get_dist(self, pos_a, pos_b):
        return int(round(((pos_a[0] - pos_b[0])**2 + (pos_a[1] - pos_b[1])**2)**(1/2), 0))
        
    def move(self):
        angle_step = math.radians(5)
        
        x, y = self.position
        x_max, y_max = self.map_size

        distance = self.generate_random_gaussian(self.mobility[0], self.mobility[1])
        distance = round(min(distance, self.energy / self.unit_energy_consumption), 0)
        self.energy -= distance * self.unit_energy_consumption
        
        angle = random.uniform(0, 2 * math.pi)

        rotation_direction = random.choice([1, -1])
        
        while True:
            x_new = x + distance * math.cos(angle)
            y_new = y + distance * math.sin(angle)
            
            if 0 <= x_new <= x_max and 0 <= y_new <= y_max:
                new_pos = [int(x_new), int(y_new)]
                break
    
            angle += rotation_direction * angle_step
        
        self.position = new_pos

    def hunt(self, prey):
        
        hun_prob = random.random()
        if 1 - self.energy < hun_prob:
            return False

        predator_power = self.generate_random_gaussian(self.fight_stat[0], self.fight_stat[1])
        prey_power = self.generate_random_gaussian(prey.fight_stat[0], prey.fight_stat[1])

        if predator_power > prey_power:

            self.energy += prey.nutrition_value - self.fight_costs
            self.energy = min(1, self.energy)
            prey.die()
            
        else:
            self.energy -= self.fight_costs
            prey.energy -= prey.fight_costs

        return True
    
    def bread(self):

        if self.gender == 'Female':
            if self.maturity[0] - self.maturity[1] <= self.age <= self.maturity[0] + self.maturity[1]:
                if self.energy >= self.min_energy_to_bread:
                    num = random.random()
                    if num <= self.fertility[0]:
                        nr_offsprings = self.generate_random_gaussian(self.fertility[1], self.fertility[2])
                        nr_offsprings = int(round(nr_offsprings, 0))
                        
                        if nr_offsprings * self.breading_cost_per_offspring <= self.energy:
                            pass
                        else:
                            nr_offsprings = int(round(self.energy // self.breading_cost_per_offspring, 0))

                        self.energy -= nr_offsprings * self.breading_cost_per_offspring

                        return nr_offsprings
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    def die(self):
        self.alive = False

    def is_alive(self):
        if self.energy <= 0:
            self.die()
            return False
        
        return self.alive

    def eat_field(self, field_nutrition_value: float):
        if self.energy + field_nutrition_value > 1:
            consumed = 1 - self.energy
            self.energy = 1
        else:
            consumed = field_nutrition_value
            self.energy += field_nutrition_value
        
        return consumed

    def get_species(self):
        return self.species
    
    def get_color(self):
        return self.color

    def get_pos(self):
        return self.position
    
    def get_feed_range(self):
        return self.feed_range

    def get_older(self):
        self.age += 1
        if self.age >= self.death_time:
            self.die()

    def print_animal(self):
        print(f"\t\tspecies:  {self.species},  color: {self.color},\n\
                age:      {self.age}, death_time: {self.death_time},\n\
                gender:   {self.gender},\n\
                energy:   {round(self.energy, 6)},\n\
                position: {self.position}")
        
    def __del__(self):
        return True