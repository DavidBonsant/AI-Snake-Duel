# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import copy
import pickle

from game import Game
from game import Player
from game import Neural_Genetic

POPULATION_SIZE = 8
GAME_LENGTH = 100
NUM_GENERATIONS = 100
NUM_TOURNAMENTS = 8
GAME_SIZE = 16


class Tournament:
    def __init__(self, population=None, pop_size=8, initial_game_length=10, game_length_step=10, max_game_length=300, num_gen=100):
        self.population = population

        if self.population is None:
            self.population = []
            for i in range(pop_size):
                self.population.append(Neural_Genetic.NN())

        self.game_length = initial_game_length
        self.game_length_step = game_length_step
        self.max_game_length = max_game_length
        self.num_gen = num_gen

    def train(self):
        for epoch in range(self.num_gen):
            print("epoch: " + str(epoch))

            self.do_tournament()

            first0 = copy.deepcopy(self.population[0])
            first1 = copy.deepcopy(self.population[0])
            first2 = copy.deepcopy(self.population[0])
            second0 = copy.deepcopy(self.population[1])
            second1 = copy.deepcopy(self.population[1])
            second2 = copy.deepcopy(self.population[1])
            third = copy.deepcopy(self.population[2])

            new_agent = Neural_Genetic.NN()

            first1.mutate(second0)
            first2.mutate2()
            second1.mutate(third)
            second2.mutate2()
            third.mutate(first0)

            self.population = [first0, first1, first2, second0, second1, second2, third, new_agent]

            if self.game_length < self.max_game_length:
                self.game_length += self.game_length_step

    # Every agent playes againts each other and are ordered by number of games won
    def do_tournament(self):
        values = [0 for i in range(len(self.population))]

        for i in range(len(self.population)):
            for j in range(i+1, len(self.population)):
                outcome = self.do_game(self.population[i], self.population[j])

                if outcome == 1:
                    values[i] += 1

                if outcome == 2:
                    values[j] += 1

        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    def do_game(self, agent1, agent2):
        g = Game.Game(GAME_SIZE, GAME_SIZE,
                      Player.Player(0, 3, 3, GAME_SIZE, GAME_SIZE, decision_maker=agent1),
                      Player.Player(1, 11, 11, GAME_SIZE, GAME_SIZE, decision_maker=agent2))

        for i in range(self.game_length):
            g.update()

            if g.done:
                return g.get_winner()

        return 0

    def get_best(self):
        self.do_tournament()

        return self.population[0]


def train_algorithm():
    tourneys = []

    for i in range(NUM_TOURNAMENTS):
        print("Starting tournament: " + str(i + 1))
        tourneys.append(Tournament())
        tourneys[i].train()
        pickle.dump(tourneys[i].get_best(), open("ai/best_nn_gen_" + str(i) + ".p", "wb"))

    final_pop = [t.get_best() for t in tourneys]

    last_tourney = Tournament(population=final_pop)
    pickle.dump(last_tourney.get_best(), open("best_nn_gen.p", "wb"))


train_algorithm()  # Note: Games are not long enough. Too many generations.
