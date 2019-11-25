# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

# Ce fichier contient la logique pour le jeu complet.
import random


class Game:
    class Cell:
        # static variables for easy grouping
        EMPTY = []
        PLAYER = [[], []]
        LAST_TO_PICKUP_APPLE = None

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.food = False
            # age > 0 means there is a snake part here.
            self.age = 0
            self.EMPTY.append(self)
            # index to specify the player
            self.player = 0

        def update(self):
            if self.age > 0:
                self.age -= 1
                if self.age == 0:
                    self.PLAYER[self.player].remove(self)
                    self.EMPTY.append(self)

        def move(self, player):
            if self.age == 0:
                self.EMPTY.remove(self)
                self.player = player.index
                self.age = player.age
                self.PLAYER[self.player].append(self)
                if self.food:
                    self.food = False
                    player.age -= -1
                    for cell in self.PLAYER[self.player]:
                        cell.age -= -1
                    random.choice(self.EMPTY).food = True
                    self.LAST_TO_PICKUP_APPLE = self.player

        # Returns the appropriate colour depending on the state
        def draw(self, bg, food, players):
            return players if self.age > 0 else food if self.food else bg

    def __init__(self, width, height, player1, player2):
        self.done = False
        self.w = width
        self.h = height
        self.p1 = player1
        self.p2 = player2
        self.board = [[self.Cell(i, j) for j in range(self.h)] for i in range(self.w)]
        # Place a piece of food
        random.choice(self.Cell.EMPTY).food = True

    def update(self):
        if self.p1.dead and self.p2.dead:
            self.done = True
            # print("Égalitée!")
        elif self.p1.dead:
            self.done = True
            # print("P2 gagne!")
        elif self.p2.dead:
            self.done = True
            # print("P1 gagne!")
        else:
            food_position = [0, 0]

            # Update cells and store current position of food
            for x, row in enumerate(self.board):
                for y, cell in enumerate(row):
                    cell.update()
                    if cell.food:
                        food_position = [x, y]

            self.update_players(food_position)

            if self.board[self.p1.x][self.p1.y].age > 0:
                self.p1.die()
            if self.board[self.p2.x][self.p2.y].age > 0:
                self.p2.die()
            if self.p1.x == self.p2.x and self.p1.y == self.p2.y:
                self.p1.die()
                self.p2.die()

            self.board[self.p1.x][self.p1.y].move(self.p1)
            self.board[self.p2.x][self.p2.y].move(self.p2)

    # Les données sont données de la perspective du serpent
    # Par défaut le serpent se dirige dans la direction [1, 0].
    # Cette direction est la direction "à l'endroit"
    # Toutes les valeurs de distance sont données %width, %height, elles sont donc positives
    # Lorsque le serpent vas dans la direction [-1, 0], les valeurs sont inversés.
    # Lorsque le serpent vas dans la direction [0, 1], x et y sont inversés

    def update_players(self, food_position):
        p1_forward = self.get_distance_to_next_wall(self.p1)
        p2_forward = self.get_distance_to_next_wall(self.p2)

        p1_left = self.get_distance_to_next_wall(self.p1, -1)
        p2_left = self.get_distance_to_next_wall(self.p2, -1)

        p1_right = self.get_distance_to_next_wall(self.p1, 1)
        p2_right = self.get_distance_to_next_wall(self.p2, 1)

        # function to avoid writing long equation multiple times
        # player is the player , x and y are the actual positions on the grid
        # 1 and -1 are squared when only the absolute value is needed
        def relativePos(player, x, y, game):
            mx = player.movement[0]
            my = player.movement[1]
            return_x = ((x * mx + y * my) - player.x) % (game.width * mx ** 2 + game.height * my ** 2)
            return_y = ((y * mx + x * my) - player.y) % (game.width * my ** 2 + game.height * mx ** 2)
            return return_x, return_y 

        p1_food_x, p1_food_y = relativePos(self.p1, food_position[0], food_position[1], self)
        p2_food_x, p2_food_y = relativePos(self.p2, food_position[0], food_position[1], self)

        p1_enemy_x, p1_enemy_y = relativePos(self.p1, self.p2.x, self.p2.y, self)
        p2_enemy_x, p2_enemy_y = relativePos(self.p2, self.p1.x, self.p1.y, self)

        self.p1.update(p1_forward, p1_left, p1_right, p1_food_x, p1_food_y, p1_enemy_x, p1_enemy_y)
        self.p2.update(p2_forward, p2_left, p2_right, p2_food_x, p2_food_y, p2_enemy_x, p2_enemy_y)

    def get_distance_to_next_wall(self, player, direction=0):
        temp_distance = 0
        forward_position = [player.x, player.y]
        player_movement = [player.movement[0], player.movement[1]]

        if direction < 0:
            player_movement = [-player_movement[1], player_movement[0]]
        elif direction > 0:
            player_movement = [player_movement[1], -player_movement[0]]

        while temp_distance < 10:
            forward_position[0] += player_movement[0]
            forward_position[1] += player_movement[1]
            forward_position[0] %= self.w
            forward_position[1] %= self.h
            temp_distance += 1

            if self.board[forward_position[0]][forward_position[1]].age > 0:
                return temp_distance

        return 10

    # Returns a 2d array with associated colours, default is ASCII characters
    def draw(self, bg='#', food='@', players='O', head1='A', head2='B'):
        canvas = [[cell.draw(bg, food, players) for cell in row] for row in self.board]
        canvas[self.p1.x][self.p1.y] = head1
        canvas[self.p2.x][self.p2.y] = head2
        return canvas

    # Returns the winner of the game
    def get_winner(self):
        # If one of the players is dead, the other won
        if self.p1.dead and not self.p2.dead:
            return 2

        if self.p2.dead and not self.p1.dead:
            return 1

        # If both are dead or none are, the longest snake won
        if self.p1.age > self.p2.age:
            return 1

        if self.p2.age > self.p1.age:
            return 2

        # else return the last snake to pick an apple
        last_player_to_apple = self.board[0][0].LAST_TO_PICKUP_APPLE

        if last_player_to_apple == self.p1:
            return 1

        if last_player_to_apple == self.p2:
            return 2

        return 0
