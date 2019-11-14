# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import time
import sys

from game import Game
from game import Player

# Fichier à exécuter
size = 16
test = Game.Game(size, size, Player.Player(0, 3, 3, size, size), Player.Player(1, 11, 11, size, size))

print("Game start!")

for i in range(100):
    test.update()
    # Default draw function returns characters but could be Hex colour codes
    canvas = test.draw()
    if i > 0:
        print("\33[" + str(len(canvas)+1) + "A")
    for line in canvas:
        print(''.join(line))
    # print on terminal
    sys.stdout.flush()
    time.sleep(0.1)
