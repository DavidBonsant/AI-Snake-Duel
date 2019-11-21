
from game import Neural_Genetic

POPULATION_SIZE = 8
GAME_LENGTH = 100
NUM_GENERATIONS = 100
NUM_TOURNAMENTS = 4


class Tournament:
    def __init__(self, pop_size=8, initial_game_length=10, game_length_step=10, max_game_length=300, num_gen=100):
        self.population = []

        for i in range(pop_size):
            self.population.append(Neural_Genetic.NN())

        self.game_length = initial_game_length
        self.game_length_step = game_length_step
        self.max_game_length = max_game_length
        self.num_gen = num_gen

    def train(self):
        for epoch in range(self.num_gen):
            pass

    # Does the basic tournament and rearranges the population from best to worst
    def do_tournament(self):
        for i in range(self.game_length):
            pass

    def get_best(self):
        pass


def train_algorithm():
    pass



