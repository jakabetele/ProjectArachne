import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import imageio.v2 as imageio

import cv2

def gen_map():
    rgb_cell_type_dict = {
        "[0, 128, 0]" : {
            "type": "grass",
            "nutrition": 0.15,
            "regeneration": 0.01,
            "mobility": 1.0,
            "color": [0, 128/255, 0]
            },
        "[0, 0, 255]" : {
            "type": "water",
            "nutrition": 0.2,
            "regeneration": None,
            "mobility": 0.25
            },
        "[128, 128, 128]" : {
            "type": "rock",
            "nutrition": 0.0,
            "regeneration": 0.0,
            "mobility": 0.0
            }
        }
    
    map_img = imageio.imread("D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/map_v00.png")
    size_x = map_img.shape[0]
    size_y = map_img.shape[1]
    
    res_all = [] 
    for x in range(0, size_x):
        for y in range(0, size_y):
            
            pixel = map_img[x][y]
            pixel_key = str(list(pixel))
            cell = rgb_cell_type_dict[pixel_key]
            res_all.append([x, y, cell["type"],
                            cell["nutrition"], cell["regeneration"],
                            cell["mobility"], cell["color"]])

    df_map_config = pd.DataFrame(res_all, columns = ["x", "y", "type", "nutrition", "regeneration", "mobility", "color"])
    df_map_config.to_pickle("D:/0xMESTERI_II_EV/2_FELEV/RL/PROJEKT/ProjectArachne/data/" + "map_v00_config.pkl")
    
gen_map()
