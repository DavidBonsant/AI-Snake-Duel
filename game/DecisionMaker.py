# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion
import random


class BasicAI:
    def __init__(self):
        pass

    def update(self, forward=0, left=0, right=0, foodAngle=0, ennemyAngle=0):
        # Utiliser random (plein de zéros pour éviter le suicide instantané)
        return random.choice([-1, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 1])
