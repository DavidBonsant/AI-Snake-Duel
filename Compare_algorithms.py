# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion
import pickle
import sys
import random

from game import Game
from game import Player
from game import BasicAI

# Paramètres du jeu
MAX_GAME_LENGTH = 100
NUM_GAMES = 100
coin = [0, 1]
gridSize = 16
ScoreByGeneration = []
# Tout les IA
AllAIByGeneration = []

print("Pulling all objects from disk.")
sys.stdout.flush()
for i in range(14,15):
    # 0 arbre de décision, 1 NN
    AllAIByGeneration.append([
            pickle.load(open("ai/Arbre de décision/Decision_Tree_best_gen_epoch%d.p"%(i*20), "rb")),
            pickle.load(open("ai/NN2_best_gen_epoch180.p", "rb"))#pickle.load(open("ai/oldNN/NN2_best_gen_epoch%d.p"%(i*20), "rb"))
        ])
    ScoreByGeneration.append([0, 0, 0])
print("Done!")
sys.stdout.flush()

for i in range(15):
    print("Simulation pour la generation %d en cours."%(i*20))
    sys.stdout.flush()
    random.shuffle(coin)
    for j in range(100):
        game = Game.Game(gridSize, gridSize,
                Player.Player(0, 3, 3, gridSize, gridSize, decision_maker=AllAIByGeneration[i][coin[0]]),
                Player.Player(1, gridSize-3, gridSize-3, gridSize, gridSize, decision_maker=AllAIByGeneration[i][coin[1]])
            )
        for k in range(MAX_GAME_LENGTH):
            game.update()
            if game.done:
                break
        win = game.get_winner()
        # 0 Arbre, 1 NN, 2 égalitée
        if win == 0:
            ScoreByGeneration[i][2]-=-1
        elif win == 1:
            ScoreByGeneration[i][coin[0]]-=-1
        elif win == 2:
            ScoreByGeneration[i][coin[1]]-=-1
    print("Arbre de décision:", ScoreByGeneration[i][0])
    print("Neural network   :", ScoreByGeneration[i][1])
    print("Égalitée         :", ScoreByGeneration[i][2])
