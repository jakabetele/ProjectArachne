import numpy as np
import pandas as pd

import json

import time

from config_dir.config_obj import foodnet_config_obj, map_color_dictionary, animals_config_obj, simulation_config_obj 

from src.Map import Map
from src.Animal import Animal
from src.Simulation import Simulation

def setup_animal_kingdom(map_size, animals_config):
    species_all = {}
    list_of_animals_all = []
    for animal_config in animals_config_obj:
        
        number = animal_config['number']
        species = {animal_config['animal']['species']: animal_config['animal']}
        species_all.update(species)

        for i in range(number):
            list_of_animals_all.append(Animal(map_size, animal_config['animal']))

    return species_all, list_of_animals_all

def main():

    df_map_config = pd.read_pickle("E:/ProjectArachne/ProjectArachne/config_dir/" + "map_v00_config.pkl")
    map_ = Map(map_color_dictionary, df_map_config)
    map_size = [map_.size_x, map_.size_y]

    foodnet = foodnet_config_obj

    species_all, list_of_animals_all = setup_animal_kingdom(map_size, animals_config_obj)

    simulation_config = simulation_config_obj
        
    simulation = Simulation(map_, foodnet, species_all,
                            list_of_animals_all, simulation_config)

    animal_state_all, map_state_all = simulation.start()

    del map_
    del simulation

    df_animal_state_all = pd.concat(animal_state_all, axis = 0)
    df_map_state_all = pd.concat(map_state_all, axis = 0)
    
    df_animal_state_all.to_csv("E:/ProjectArachne/simulation_history_data/" + "animal_state_all.csv")
    df_map_state_all.to_csv("E:/ProjectArachne/simulation_history_data/" + "map_state_all.csv")
            
main()
