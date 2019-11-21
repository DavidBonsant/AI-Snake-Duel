# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

from game import BasicAI


# Ce fichier est l'objet de base pour un joueur
# -- En entrée:
#       x: la position en x du joueur
#       y: la position en y du joueur
#       width: la largeur du jeu
#       length: la longueur du jeu
#       age: la longueur du serpent en fonction du nombre de pommes amassées
#       decision_maker: l'algorithme qui décide de la prochaine direction à prendre
#           cet algorithme doit contenir une fonction update() qui retourne 0, 1 ou -1 selon la décision
class Player:
    def __init__(self, index, x, y, width, length, age=5, decision_maker=None):
        self.dead = False
        self.index = index
        self.x = x
        self.y = y
        # Vecteur pour la direction
        self.movement = [1, 0]
        self.width = width
        self.length = length
        self.age = age
        self.ai = decision_maker

        if decision_maker is None:
            self.ai = BasicAI.BasicAI()

    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        self.move(self.ai.update(forward, left, right, pomme_x, pomme_y, enemy_x, enemy_y))

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
