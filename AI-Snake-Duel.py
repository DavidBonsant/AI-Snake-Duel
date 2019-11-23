# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import time
import sys

from game import Game
from game import Player

from ai_gui import GameRenderer

# Fichier à exécuter
# Longeur maximale d'une partie
MAX_LENGTH = 100
# Créer la partie
size = 16
test = Game.Game(size, size, Player.Player(0, 3, 3, size, size), Player.Player(1, 11, 11, size, size))

print("Game start!")
g = GameRenderer(test)
g.render(MAX_LENGTH)
print("Winner: " + str(test.get_winner()))


def run_game_without_gui():
    for i in range(MAX_LENGTH):
        test.update()

        if test.done:
            break
        else:
            # Default draw function returns characters but could be Hex colour codes
            canvas = test.draw()
            if i > 0:
                # Effacer la grille
                print("\33[" + str(len(canvas) + 1) + "A")
            for line in canvas:
                print(''.join(line))
            # print on terminal
            sys.stdout.flush()
            time.sleep(0.1)

# Exemple de comment ouvrir un AI
# ai = pickle.load(open("ai/AI_NAME.p", "rb"))
