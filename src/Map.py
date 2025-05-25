import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

class Map(object):

    def __init__(self, map_color_dictionary: dict, df_map_config: pd.DataFrame):
        self.df_map = df_map_config.copy()
        
        self.size_x = self.df_map['x'].max() + 1
        self.size_y = self.df_map['y'].max() + 1

        #["x", "y", "type", "nutrition", "regeneration", "mobility", "color"]
        
        x_coords, y_coords = self.df_map['x'].values,self.df_map['y'].values

        self.type_names = list(map_color_dictionary.keys())
        type_to_int = {name: i for i, name in enumerate(self.type_names)}
        self.type_grid = np.zeros((self.size_x, self.size_y), dtype=np.int8)
        self.nutrition_grid = np.zeros((self.size_x, self.size_y), dtype=np.float32)
        self.regeneration_grid = np.zeros_like(self.nutrition_grid)

        self.max_nutrition_grid = np.zeros_like(self.nutrition_grid)

        self.type_grid[x_coords, y_coords] = self.df_map['type'].map(type_to_int).values
        self.nutrition_grid[x_coords, y_coords] = self.df_map['nutrition'].values
        self.regeneration_grid[x_coords, y_coords] = self.df_map['regeneration'].values
        
        max_nutrition_map = {key: val['max'] for key, val in map_color_dictionary.items()}
        mapped_max_series = self.df_map['type'].map(max_nutrition_map)
        self.max_nutrition_grid[x_coords, y_coords] = mapped_max_series.values

        self.update_alpha()

    def update_alpha(self):
        with np.errstate(divide='ignore', invalid='ignore'):
            alpha = self.nutrition_grid / self.max_nutrition_grid
        
        self.df_map['alpha'] = alpha[self.df_map['x'].values, self.df_map['y'].values].clip(0, 1)

    def regenerate_grass(self):
        self.nutrition_grid += self.regeneration_grid
        np.minimum(self.nutrition_grid, self.max_nutrition_grid, out=self.nutrition_grid)
        
        self.df_map['nutrition'] = self.nutrition_grid[self.df_map['x'].values, self.df_map['y'].values]

        self.update_alpha()

    def get_state(self) -> pd.DataFrame:
        return self.df_map.copy()

"""
class Map(object):
    def __init__(self, map_color_dictionary: dict, df_map_config: pd.DataFrame):
        
        self.map_color_dictionary = map_color_dictionary

        self.size_x = df_map_config['x'].max() + 1
        self.size_y = df_map_config['y'].max() + 1

        self.df_map = df_map_config
        
        self.df_map['alpha'] = self.df_map.apply(lambda x: x["nutrition"]/ 
                                                           self.map_color_dictionary[x['type']]['max'], 
                                                       axis = 1)
    
    def regenare_grass(self):
        self.df_map["nutrition"] = self.df_map.apply(lambda x: min(x["nutrition"] + x["regeneration"], 
                                                               self.map_color_dictionary[x['type']]['max']), 
                                                     axis = 1)
        
        self.df_map['alpha'] = self.df_map.apply(lambda x: x["nutrition"]/ 
                                                           self.map_color_dictionary[x['type']]['max'], 
                                                 axis = 1)

        return True
    
    def get_state(self):        
        return pd.DataFrame(self.df_map)

    def __del__(self):
        return True"""
                    
