# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion
import pickle
import time
import sys

from game import Game
from game import Player
from game import BasicAI

from ai_gui import GameRenderer

# Fichier à exécuter
# Longeur maximale d'une partie
MAX_LENGTH = 100
# Créer la partie
size = 16
# utiliser le cmd ou le gui
cmd = True

# Exemple de comment ouvrir un AI
ai1 = pickle.load(open("ai/Arbre de décision/Decision_Tree_best_gen_epoch280.p", "rb"))
ai2 = pickle.load(open("ai/NN2_best_gen_epoch180.p", "rb"))

test = Game.Game(size, size, Player.Player(0, 3, 3, size, size, decision_maker=ai1),
                 Player.Player(1, size-3, size-3, size, size, decision_maker=ai2))

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

print("Game start!")
if cmd:
    run_game_without_gui()
else:
    g = GameRenderer(test)
    g.render(MAX_LENGTH)
print("Winner: " + str(test.get_winner()))
print(test.get_score(2))
