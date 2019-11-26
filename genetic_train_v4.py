# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import copy
import pickle
from statistics import mean

from game import Game
from game import Player
from game import Neural_Genetic
from game import BasicAI
import random

POPULATION_SIZE = 8
GAME_LENGTH = 100
NUM_GENERATIONS = 100
NUM_TOURNAMENTS = 8
GAME_SIZE = 16


class Tournament:
    def __init__(self, population=None, pop_size=50, initial_game_length=50, game_length_step=0,
                 max_game_length=1000, num_gen=20, training_ai=BasicAI.ImmobileAI(), num_gen_before_ai_change=40):
        self.population = population

        if self.population is None:
            self.population = []
            for i in range(pop_size):
                self.population.append(Neural_Genetic.NN())

        self.game_length = initial_game_length
        self.game_length_step = game_length_step
        self.max_game_length = max_game_length
        self.num_gen = num_gen
        self.training_ai = training_ai
        self.num_gen_before_ai_change = num_gen_before_ai_change

    def train(self):
        for epoch in range(self.num_gen):
            print("epoch: " + str(epoch))

            self.do_train_to_get_apple()

            # new_agent = Neural_Genetic.NN()
            new_pop = []

            for i in range(len(self.population) // 5):
                new_pop.extend(self.breed(self.population[i], self.population[i+1], epoch))

            # To track temporary progress
            pickle.dump(self.population[0], open("temp/best_nn_gen.p", "wb"))

            while len(new_pop) < len(self.population):
                new_pop.append(copy.deepcopy(self.population[
                                                 random.randint(len(self.population) // 5 + 1, len(self.population)-1)]))

            self.population = new_pop

            if self.game_length < self.max_game_length:
                self.game_length += self.game_length_step

    def breed(self, main_agent, second_agent, epoch):
        first = copy.deepcopy(main_agent)
        second = copy.deepcopy(main_agent)
        third = copy.deepcopy(main_agent)

        first.mutate(second_agent, epoch//2)
        second.mutate2(epoch//2)
        third.mutate2(epoch//2)

        return [main_agent, first, second, third]

    # Every agent playes againts each other and are ordered by number of games won
    # Agents play 2 times: Once as A, once as B
    def do_tournament(self):
        values = [0 for i in range(len(self.population))]

        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                outcome = self.do_game(self.population[i], self.population[j]).get_winner()

                if outcome == 1:
                    values[i] += 1

                if outcome == 2:
                    values[j] += 1

        print(values)
        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    def do_train_to_get_apple(self):
        values = [0 for i in range(len(self.population))]

        for i in range(len(self.population)):
            values[i] = self.do_game(self.population[i], self.training_ai).get_score(1)

        print(mean(values))
        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    def do_game(self, agent1, agent2):
        g = Game.Game(GAME_SIZE, GAME_SIZE,
                      Player.Player(0, 3, 3, GAME_SIZE, GAME_SIZE, decision_maker=agent1),
                      Player.Player(1, 5, 5, GAME_SIZE, GAME_SIZE, decision_maker=agent2))

        for i in range(self.game_length):
            g.update()

            if g.done:
                return g

        return g

    def get_best(self):
        self.do_tournament()

        return self.population[0]


def train_algorithm():
    tourneys = []

    for i in range(1):
        print("Starting tournament: " + str(i + 1))
        tourneys.append(Tournament())
        tourneys[i].train()
        pickle.dump(tourneys[i].get_best(), open("ai2/best_nn_gen_" + str(i) + ".p", "wb"))

    '''final_pop = [t.get_best() for t in tourneys]

    last_tourney = Tournament(population=final_pop)
    pickle.dump(last_tourney.get_best(), open("ai2/best_nn_gen.p", "wb"))'''


train_algorithm()
