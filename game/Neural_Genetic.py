import math
import random
import numpy as np


MAX_ITERATION = 4000
POP_SIZE = 8
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8

NUMBER_OF_HIDDEN_LAYERS = 10


def sigmoid(x):
    return math.tanh(x)


def randomize_matrix(matrix, a, b):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.uniform(a, b)


class NN:
    def __init__(self, number_hidden):
        self.number_input = 7
        self.number_hidden = number_hidden
        self.number_output = 3
        self.ai = [1.0] * self.number_input
        self.ah = [1.0] * self.number_hidden
        self.ao = [1.0] * self.number_output
        self.wi = [[0.0] * self.number_hidden for i in range(self.number_input)]
        self.wo = [[0.0] * self.number_output for j in range(self.number_hidden)]
        randomize_matrix(self.wi, 0.0, 1.0)
        randomize_matrix(self.wo, 0.0, 1.0)

    def run(self, inputs):
        if len(inputs) != self.number_input:
            print('incorrect number of inputs')
        for i in range(self.number_input):
            self.ai[i] = inputs[i]
        for j in range(self.number_hidden):
            self.ah[j] = sigmoid(sum([self.ai[i] * self.wi[i][j] for i in range(self.number_input)]))
        for k in range(self.number_output):
            self.ao[k] = sigmoid(sum([self.ah[j] * self.wo[j][k] for j in range(self.number_hidden)]))
        return self.ao

    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        inputs = [forward, left, right, pomme_x, pomme_y, enemy_x, enemy_y]

        output = self.run(inputs)

        choice = output.index(max(output))

        if choice == 0:
            return -1

        if choice == 1:
            return 0

        return 1

    def mutate(self, other_nn):
        for y in range(len(self.wi)):
            for x in range(len(self.wi[y])):
                if random.randint(0, 1) == 1:
                    self.wi[y][x] = other_nn.wi[y][x]

    def mutate2(self):
        for y in range(len(self.wi)):
            for x in range(len(self.wi[y])):
                if random.randint(0, 1) == 1:
                    self.wi[y][x] += random.uniform(0.0, 1.0)


n = NN(NUMBER_OF_HIDDEN_LAYERS)
n2 = NN(NUMBER_OF_HIDDEN_LAYERS)
print(n.update())
print(n2.update())

n.mutate(n2)
n2.mutate(n)

print(n.update())
print(n2.update())

