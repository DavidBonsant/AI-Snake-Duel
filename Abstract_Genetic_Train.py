
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


class ScoringSystem:
    def __init__(self, points_forward_apple=1, points_backwards_apple=-3, points_collect_apple=20, points_win=50):
        self.score = 0
        self.last_dist = 0
        self.points_forward_apple = points_forward_apple
        self.points_backwards_apple = points_backwards_apple
        self.points_collect_apple = points_collect_apple
        self.points_win = points_win

    def update(self, pomme_pos, player_pos):
        new_dist = (pomme_pos[0] - player_pos[0])**2 + (pomme_pos[1] - player_pos[1])**2

        if self.last_dist != 0:
            # Lose X points when going away from apple
            if new_dist > self.last_dist:
                self.score += self.points_backwards_apple
            else:
                # Gains Y point when going towards the apple
                self.score += self.points_forward_apple

        self.last_dist = new_dist

    def finalize(self, player, won):
        # wins 20 points per apple collected
        self.score += (player.age - 5) * self.points_collect_apple

        # Looses 50 points if the player lost.
        if won:
            self.score += self.points_win


class Tournament:
    def __init__(self, agent_class, population=None, pop_size=50, initial_game_length=20, game_length_step=5,
                 max_game_length=200, num_gen=100, scoring_system=ScoringSystem):
        self.population = population

        if self.population is None:
            self.population = []
            for i in range(pop_size):
                self.population.append(agent_class())

        self.game_length = initial_game_length
        self.game_length_step = game_length_step
        self.max_game_length = max_game_length
        self.num_gen = num_gen

        self.all_training_ai = [BasicAI.AfraidAI(), BasicAI.RandomAI(), BasicAI.ImmobileAI(), BasicAI.CirlceAI()]

        self.mean_values = []
        self.scoring_system = scoring_system

    def train(self):
        for epoch in range(self.num_gen):
            print("epoch: " + str(epoch))

            self.do_train_to_get_apple()

            new_pop = []

            for i in range(len(self.population) // 5):
                new_pop.extend(self.breed(self.population[i], self.population[i+1], epoch))

            # To track temporary progress, save best AI yet every 20 epoch
            if epoch % 20 == 0:
                pickle.dump(self.population[0], open("temp/best_nn_gen_epoch" + str(epoch) + ".p", "wb"))

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

        first.set_mutate_rate(epoch//2)
        first.cross(second_agent)

        second.set_mutate_rate(epoch//2)
        second.mutate1()

        third.set_mutate_rate(epoch//2)
        third.mutate2()

        return [main_agent, first, second, third]

    # Every agent plays againts each other and are ordered by number of games won
    def do_tournament(self):
        values = [0 for i in range(len(self.population))]

        # Won't do a tournament bigger than 8
        for i in range(min(8, len(self.population))):
            for j in range(i + 1, min(8, len(self.population))):
                outcome = self.do_game(self.population[i], self.population[j]).get_winner()

                if outcome == 1:
                    values[i] += 1

                if outcome == 2:
                    values[j] += 1

        print(values)
        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    # Train agents to get a good score for the game
    def do_train_to_get_apple(self):
        values = [0 for i in range(len(self.population))]

        for i in range(len(self.population)):
            for ai in self.all_training_ai:
                values[i] += self.do_game(self.population[i], ai).get_score(player_num=1)

        print(mean(values))
        self.mean_values.append(mean(values))
        self.population = [x for (y, x) in sorted(zip(values, self.population), key=lambda pair: pair[0], reverse=True)]

    def do_game(self, agent1, agent2):
        g = Game.Game(GAME_SIZE, GAME_SIZE,
                      Player.Player(0, 3, 3, GAME_SIZE, GAME_SIZE, decision_maker=agent1),
                      Player.Player(1, 11, 11, GAME_SIZE, GAME_SIZE, decision_maker=agent2),
                      scoring_system=self.scoring_system)

        for i in range(self.game_length):
            g.update()

            if g.done:
                return g

        return g

    def get_best(self):
        print(self.mean_values)
        self.do_tournament()

        return self.population[0]


# Trains a set of algorithms with desired algo class
def train_algorithm(algorithm):
    tourneys = []

    for i in range(1):
        print("Starting tournament: " + str(i + 1))
        tourneys.append(Tournament(algorithm, pop_size=50, initial_game_length=20, game_length_step=5,
                                   max_game_length=200, num_gen=100, scoring_system=ScoringSystem))
        tourneys[i].train()
        pickle.dump(tourneys[i].get_best(), open(str(algorithm.__name__) + "/best_gen_tourney_" + str(i) + ".p", "wb"))

    # final_pop = [t.get_best() for t in tourneys]

    # last_tourney = Tournament(algorithm, population=final_pop)
    # pickle.dump(last_tourney.get_best(), open(str(algorithm.__name__) + "/best.p", "wb"))


train_algorithm(Neural_Genetic.NN)
