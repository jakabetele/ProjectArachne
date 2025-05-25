import warnings
warnings.filterwarnings("ignore")

class FoodNet(object):

    def __init__(self, species: int, relational_list: list):
        self.relational_list = relational_list
        self.relational_matrix = [[[] for i in range(species)] for i in range(species)]

        for i, pray_list in enumerate(relational_list):
            for prey in pray_list:
                self.relational_matrix[i][prey] = True