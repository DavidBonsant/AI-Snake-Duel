import math
import random
import numpy as np

NUMBER_OF_HIDDEN_LAYERS = 10


def sigmoid(x):
    return math.tanh(x)


def relu(x):
    return max(0, x)


def randomize_matrix(matrix, a, b):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.uniform(a, b)


class NN:
    def __init__(self, number_hidden=1):
        self.number_input = 7
        self.number_hidden = number_hidden
        self.number_output = 3
        self.ai = [1.0] * self.number_input
        self.ah = [1.0] * self.number_hidden
        self.ao = [1.0] * self.number_output
        self.wi = [[0.0] * self.number_hidden for i in range(self.number_input)]
        self.wo = [[0.0] * self.number_output for j in range(self.number_hidden)]
        randomize_matrix(self.wi, -2.0, 2.0)
        randomize_matrix(self.wo, -2.0, 2.0)

        self.mutation_rate = 2

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

    def cross(self, other_nn):
        for y in range(len(self.wi)):
            for x in range(len(self.wi[y])):
                if random.randint(0, self.mutation_rate) == 0:
                    self.wi[y][x] = other_nn.wi[y][x]

        for y in range(len(self.wo)):
            for x in range(len(self.wo[y])):
                if random.randint(0, self.mutation_rate) == 0:
                    self.wo[y][x] = other_nn.wo[y][x]

    def set_mutate_rate(self, epoch):
        self.mutation_rate = (epoch+1) // 10

    def mutate1(self):
        for y in range(len(self.wi)):
            for x in range(len(self.wi[y])):
                if random.randint(0, self.mutation_rate) == 0:
                    self.wi[y][x] += random.uniform(-2.0, 2.0)

    def mutate2(self):
        for y in range(len(self.wo)):
            for x in range(len(self.wo[y])):
                if random.randint(0, self.mutation_rate) == 0:
                    self.wo[y][x] += random.uniform(-2.0, 2.0)


class NN2(NN):
    def __init__(self):
        super().__init__(number_hidden=10)

    def run(self, inputs):
        if len(inputs) != self.number_input:
            print('incorrect number of inputs')
        for i in range(self.number_input):
            self.ai[i] = inputs[i]
        for j in range(self.number_hidden):
            self.ah[j] = relu(sum([self.ai[i] * self.wi[i][j] for i in range(self.number_input)]))
        for k in range(self.number_output):
            self.ao[k] = relu(sum([self.ah[j] * self.wo[j][k] for j in range(self.number_hidden)]))
        return self.ao

