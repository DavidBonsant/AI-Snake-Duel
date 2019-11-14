# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

# Ce fichier contient la logique pour le jeu complet.
import random

class Game:
    class Cell:
        # static variables for easy grouping of diffrent states
        EMPTY = []
        PLAYER = [[],[]]

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.food = False
            # 0 is empty or food, or else there is a snake part here.
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
            self.player = player.index
            self.age = player.age
            self.EMPTY.remove(self)
            self.PLAYER[self.player].append(self)
            if self.food:
                self.food = False
                player.age-=-1
                for cell in self.PLAYER[self.player]:
                    cell.age-=-1
                random.choice(EMPTY).food = True

            

        # Returns the appropriate colour depending on the state
        def draw(self, bg, food, players):
            return players if self.age > 0 else food if self.food else bg


    def __init__(self, width, height, player1, player2):
        self.w = width
        self.h = height
        self.p1 = player1
        self.p2 = player2
        self.board = [[self.Cell(i, j) for j in range(self.h)] for i in range(self.w)]

    def update(self):
        for row in self.board:
            for cell in row:
                cell.update()

        self.p1.update()
        self.p2.update()

        if self.board[self.p1.x][self.p1.y].age > 0:
            self.p1.die()
        if self.board[self.p2.x][self.p2.y].age > 0:
            self.p1.die()

        self.board[self.p1.x][self.p1.y].move(self.p1)
        self.board[self.p2.x][self.p2.y].move(self.p2)

    # Returns a 2d array with associated colours, default is ASCII characters
    def draw(self, bg='# ', food='@ ', players='O ', head1='A ', head2='B '):
        canvas = [[cell.draw(bg, food, players) for cell in row] for row in self.board]
        canvas[self.p1.x][self.p1.y] = head1
        canvas[self.p2.x][self.p2.y] = head2
        return canvas
