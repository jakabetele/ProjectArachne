foodnet_config_obj = {
    "lion" : ["zebra", "gazelle", "rabbit"],
    "cheetah" : ["zebra", "gazelle", "rabbit"],
    "zebra": ["grass"],
    "gazelle" : ["grass"],
    "rabbit": ["grass"]
    
}

map_color_dictionary = {
    "grass" : {
        "color": [0, 128, 0],
        "max" : 0.15
        }
}

simulation_config_obj = {
    "run_type": "endless", # limited / endless
    "simulation_steps" : 20,
    "min_species": 5,
    "print_info": True,
    "generate_simulation_gif" : True,
    "frame_duration" : 0.5,
    "save_path" : "D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/",
    "plot_config_obj" : {
        "figsize" : [12, 10]
    }
}

animals_config_obj = [
            {
             "number": 20,
             "animal": {"species" : "lion",                  #The species name
                        "color" : "orange",                  #The color of species on the simualtion gif
                        "initial_energy" : 0.8,              #The energy whith which the animal is born
                        "nutrition_value" : 0.8,             #The energy value for predator
                        "feed_range" : 10.0,                 #The distance in which it can eat from field or hunt
                        "life_expectancy" : (25, 3),         #The expected life length and the std coefficient
                        "maturity" : (15, 5),                #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.2, 2, 0.33),         #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01,#The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (10, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.01,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (25.0, 3),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            },
            {
             "number": 20,
             "animal": {"species" : "cheetah",                #The species name
                        "color" : "yellow",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.75,              #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 15.0,                  #The distance in which it can eat from field or hunt
                        "life_expectancy" : (18, 3),         #The expected life length and the std coefficient
                        "maturity" : (10, 3),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.2, 2, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (12, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.005,   #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (16.0, 2),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.05                  #The cost of a fight
                        }
            },
            {
             "number": 50,
             "animal": {"species" : "zebra",               #The species name
                        "color" : "black",                   #The color of species on the simualtion gif
                        "initial_energy" : 0.6,             #The energy whith which the animal is born
                        "nutrition_value" : 0.9,             #The energy value for predator
                        "feed_range" : 1.0,                 #The distance in which it can eat from field or hunt 
                        "life_expectancy" : (20, 3),         #The expected life length and the std coefficient
                        "maturity" : (10, 5),                #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.2, 2, 0.33),         #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01,#The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (15, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.011,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (22.0, 3),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.10                  #The cost of a fight
                        }
            },
            {
             "number": 50,
             "animal": {"species" : "gazelle",               #The species name
                        "color" : "chocolate",                   #The color of species on the simualtion gif
                        "initial_energy" : 0.6,             #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 1.0,                 #The distance in which it can eat from field or hunt 
                        "life_expectancy" : (20, 3),         #The expected life length and the std coefficient
                        "maturity" : (8, 2),                #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.2, 2, 0.33),         #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01,#The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (20, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.008,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (15.0, 3),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.15                 #The cost of a fight
                        }
            },
            {
             "number": 100,
             "animal": {"species" : "rabbit",                #The species name
                        "color" : "gray",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.5,              #The energy whith which the animal is born
                        "nutrition_value" : 0.25,             #The energy value for predator
                        "feed_range" : 1.0,                  #The distance in which it can eat from field or hunt
                        "life_expectancy" : (8, 2),         #The expected life length and the std coefficient
                        "maturity" : (3, 5),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.2, 4, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.02, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (5, 1),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.0526,   #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (10.0, 1),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.05                  #The cost of a fight
                        }
            }
]

"""
foodnet_config_obj = {
    "lion" : ["wildcat", "rabbit"],
    "wildcat": ["rabbit"],
    "rabbit": ["grass"]
}

animals_config_obj = [
            {
             "number": 150,
             "animal": {"species" : "rabbit",                #The species name
                        "color" : "gray",                    #The color of species on the simualtion gif
                        "initial_energy" : 0.5,              #The energy whith which the animal is born
                        "nutrition_value" : 0.5,             #The energy value for predator
                        "feed_range" : 1.0,                  #The distance in which it can eat from field or hunt
                        "life_expectancy" : (15, 3),         #The expected life length and the std coefficient
                        "maturity" : (9, 3),                 #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.5, 4, 1),           #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.5,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.1, #The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (14, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.008,   #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (10.0, 1),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            },
            {
             "number": 30,
             "animal": {"species" : "wildcat",               #The species name
                        "color" : "black",                   #The color of species on the simualtion gif
                        "initial_energy" : 0.75,             #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 15.0,                 #The distance in which it can eat from field or hunt 
                        "life_expectancy" : (20, 3),         #The expected life length and the std coefficient
                        "maturity" : (10, 2),                #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.4, 2, 0.33),         #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01,#The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (15, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.010,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (19.0, 4),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            }
            ,
            {
             "number": 20,
             "animal": {"species" : "lion",                  #The species name
                        "color" : "orange",                  #The color of species on the simualtion gif
                        "initial_energy" : 0.8,              #The energy whith which the animal is born
                        "nutrition_value" : 0.6,             #The energy value for predator
                        "feed_range" : 15.0,                 #The distance in which it can eat from field or hunt
                        "life_expectancy" : (25, 3),         #The expected life length and the std coefficient
                        "maturity" : (12, 2),                #The mean time when it can reproduce and the +- coefficients
                        "fertility" : (0.3, 2, 0.33),         #The probability to reproduce, the expected offsprings and the std coefficient for this
                        "min_energy_to_bread" : 0.1,         #The minimum energy level for getting pregnant
                        "breading_cost_per_offspring" : 0.01,#The cost of energy for every living offspring righ after pregnancy
                        "mobility" : (15, 3),                #The expected distance to moove in a turn and the std coefficient
                        "unit_energy_consumption" : 0.010,    #The consumed energy for every unit distance done in a turn
                        "fight_stat" : (25.0, 4),            #The expected fight power in a fight and std coefficient
                        "fight_costs" : 0.1                  #The cost of a fight
                        }
            }
]
"""
