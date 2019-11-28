# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion
import random


class RandomAI:
    def __init__(self):
        pass

    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        # Utiliser random (plein de zéros pour éviter le suicide instantané)
        return random.choice([-1, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 1])


class ImmobileAI:
    def __init__(self):
        pass

    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        # Toujours continuer tout droit
        return 0


class AfraidAI:
    def __init__(self):
        pass

    # If there is a wall in front of me, I will avoid it
    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        if forward < 2:
            if left > 1:
                return -1
            if right > 1:
                return 1

        return 0
