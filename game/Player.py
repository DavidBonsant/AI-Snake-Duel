# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import random

# Ce fichier est l'objet de base pour un joueur
class Player:
    def __init__(self, index, x, y, width, length, age=5):
        self.dead = False
        self.index = index
        self.x = x
        self.y = y
        # Vecteur pour la direction
        self.movement = [1,0]
        self.width=width
        self.length=length
        self.age = age

    def update(self, forward=0, left=0, right=0, foodAngle=0, ennemyAngle=0):
        self.move(self.calculate())

    def move(self, direction):
        # Si direction = 0, pas de rotation, sinon rotation de 90 degrés
        if direction < 0:
            self.movement = [-self.movement[1], self.movement[0]]
        elif direction > 0:
            self.movement = [self.movement[1], -self.movement[0]]
        # moving logic
        self.x += self.movement[0]
        self.y += self.movement[1]
        # wrap around
        self.x %= self.width
        self.y %= self.length

    def die(self):
        self.dead = True

    # Fonction à modifier selon l'algorithme choisi
    def calculate(self, forward=0, left=0, right=0, foodAngle=0, ennemyAngle=0):
        # Utiliser random (plein de zéros pour éviter le suicide instantané)
        return random.choice([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
