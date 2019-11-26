# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import copy
import pickle
import sys
import random

from game import Game
from game import Player
from game import Decision_Tree_Genetic

POPULATION_SIZE = 128
GAME_LENGTH = 100
NUM_GENERATIONS = 50
NUM_TOURNAMENTS = 20
GAME_SIZE = 16


class Tournament:
    def __init__(self, best = None, population=None, pop_size=8, initial_game_length=10, game_length_step=10, max_game_length=300, num_gen=100):
        self.population = population

        if self.population is None:
            self.population = []
            for i in range(pop_size):
                self.population.append(Decision_Tree_Genetic.Decision_Tree())

        self.best = best     
        if self.best is None:
            self.best = Decision_Tree_Genetic.Decision_Tree()

        self.game_length = initial_game_length
        self.game_length_step = game_length_step
        self.max_game_length = max_game_length
        self.num_gen = num_gen

    def train(self):
        for epoch in range(self.num_gen):
            print("epoch: " + str(epoch))
            sys.stdout.flush()

            self.do_tournament()
            newGeneration = []
            # Garder le top 25%
            for i in range(len(self.population)//4):
                newGeneration.append(copy.deepcopy(self.population[i]))
            # Effectuer des croisements
            for i in range(len(self.population)//4):
                newGeneration.append(copy.deepcopy(self.population[i]))
                if i%2 == 1:
                    newGeneration[-1].cross(newGeneration[-2])
            # Mutations de poids
            for i in range(len(self.population)//4):
                newGeneration.append(copy.deepcopy(self.population[i]).mutate1())
            # Mutations de structure
            i=0
            while len(newGeneration) < len(self.population) - 1:
                i-=-1
                newGeneration.append(copy.deepcopy(self.population[i]).mutate2())
            # Un aléatoire juste au cas
            newGeneration.append(Decision_Tree_Genetic.Decision_Tree())

            self.population = newGeneration

            if self.game_length < self.max_game_length:
                self.game_length += self.game_length_step

    # Every agent plays againts each other and are ordered by number of games won
    def do_tournament(self):
        values = [0 for i in range(len(self.population))]

        for i in range(len(self.population)):
            outcome = self.do_game(self.population[i], self.best)
            if outcome == 1:
                values[i] += 2
            elif outcome == 0:
                values[i] += 1

        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    def do_game(self, agent1, agent2):
        g = Game.Game(GAME_SIZE, GAME_SIZE,
                      Player.Player(0, 3, 3, GAME_SIZE, GAME_SIZE, decision_maker=agent1, movement=random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])),
                      Player.Player(1, 11, 11, GAME_SIZE, GAME_SIZE, decision_maker=agent2, movement=random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])))

        for i in range(self.game_length):
            g.update()

            if g.done:
                return g.get_winner()
        # Update later for victory by score
        return g.get_winner()

    def get_best(self):
        self.do_tournament()

        return self.population[0]


def train_algorithm():
    tourneys = []
    best = None

    for i in range(NUM_TOURNAMENTS):
        tourney = Tournament(best=best, pop_size=POPULATION_SIZE, initial_game_length=min(5+i*NUM_GENERATIONS*1, GAME_LENGTH), game_length_step=1, max_game_length=GAME_LENGTH, num_gen=NUM_GENERATIONS)
        tourney.train()
        best = tourney.population[0]
        pickle.dump(tourney.get_best(), open("ai/best_decision_tree" + str(i) + ".p", "wb"))
        print("Ronde", i, "enregistrée")

train_algorithm()
