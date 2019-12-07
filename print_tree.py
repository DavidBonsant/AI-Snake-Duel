# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion
import pickle
#from game import Decision_Tree_Genetic

ATTRIBUTES = ["forward", "left", "right", "pomme_x", "pomme_y", "enemy_x", "enemy_y"]

def print_tree(node, indent=" "):
    if isinstance(node, int):
        print(indent[:-1]+ '|-(', node, ')')
    else:
        print(indent[:-1]+'|-', ATTRIBUTES[node.index])
        for child in node.children:
            nextIndent = indent
            if child == node.children[-1]:
                nextIndent = nextIndent+" "
            else:
                nextIndent = nextIndent+"|"
            print_tree(child, nextIndent)

print_tree(pickle.load(open("ai/Arbre de décision/Decision_Tree_best_gen_epoch200.p", "rb")).root)
