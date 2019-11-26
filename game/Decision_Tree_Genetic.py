# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

import random

BOARD_SIZE = 16

class Decision_Tree:
    class Node:
        # Static variable for input ranges
        INPUT_RANGES = [[0,BOARD_SIZE],[0,BOARD_SIZE],[0,BOARD_SIZE],[1-BOARD_SIZE,BOARD_SIZE],[1-BOARD_SIZE,BOARD_SIZE],[1-BOARD_SIZE,BOARD_SIZE],[1-BOARD_SIZE,BOARD_SIZE], [1-BOARD_SIZE,BOARD_SIZE]]

        # index is index for param array
        # child is default child (can be node or leaf value)
        def __init__(self, index, child, parent=None):
            self.index = index
            self.parent = None
            self.branching = []
            self.children = [child]
            if isinstance(child, Decision_Tree.Node):
                child.parent = self

        def run(self, params):
            for i, branch in enumerate(self.branching):
                if params[self.index] <= branch:
                    return self.children[i].run(params) if isinstance(self.children[i], Decision_Tree.Node) else self.children[i]
            last = len(self.children)-1
            return self.children[last].run(params) if isinstance(self.children[last], Decision_Tree.Node) else self.children[last]

        # Add a new node with random weight(if not already there)
        def add(self, node):
            # if new random branch value already exist, ignore the add. 
            val = random.randrange(self.INPUT_RANGES[self.index][0], self.INPUT_RANGES[self.index][1])
            if node not in self.children and val not in self.branching:
                self.branching.append(val)
                self.branching.sort()
                self.children.insert(self.branching.index(val), node)
                if isinstance(node, Decision_Tree.Node):
                    node.parent = self

        # Removes child and returns it(if it exists)
        def remove(self, node):
            if node in self.children and len(self.children) > 1:
                if isinstance(node, Decision_Tree.Node):
                    node.parent = None
                i = self.children.index(node)
                if i < len(self.branching):
                    self.branching.pop(i)
                return self.children.pop(i)
            return None

        # Swap child n1 with child n2 of node other (other is self by default)
        # Can swap from another tree altogether.
        def swap(self, n1, n2, other=None):
            if other == None:
                other = self
            # check if nodes are actually valid
            if n1 in self.children and n2 in other.children:
                self.children.insert(self.children.index(n1), n2)
                other.children.insert(other.children.index(n2), n1)
                self.children.remove(n1)
                other.children.remove(n2)
                if isinstance(n1, Decision_Tree.Node):
                    n1.parent = other
                if isinstance(n2, Decision_Tree.Node):
                    n2.parent = self

        # shuffle one random value of branch and reorder the array.
        def adjust(self, recursive=False):
            val = random.randrange(self.INPUT_RANGES[self.index][0], self.INPUT_RANGES[self.index][1])
            if val not in self.branching and len(self.branching) > 0:
                self.branching[random.randrange(len(self.branching))] = val
                self.branching.sort()
            if recursive:
                for child in self.children:
                    if isinstance(child, Decision_Tree.Node):
                        child.adjust(True)

        # Returns an array of all nodes
        def getNodes(self):
            nodes = [self]
            for child in self.children:
                if isinstance(child, Decision_Tree.Node):
                    nodes.extend(child.getNodes())
            return nodes

    def __init__(self):
        self.root = self.Node(0, 0)
        nodes = []
        # Construct a random tree
        for i in range(0, 7):
            nodes.append(self.Node(i, random.randrange(-1, 2)))
            if random.randrange(3) == 1:
                nodes[i].add(random.randrange(-1, 2))
        while len(nodes) > 1:
            n = nodes.pop(random.randrange(len(nodes)))
            nodes[random.randrange(len(nodes))].add(n)
        self.root.add(nodes[0])

    def update(self, forward=0, left=0, right=0, pomme_x=0, pomme_y=0, enemy_x=0, enemy_y=0):
        return self.root.run([forward, left, right, pomme_x, pomme_y, enemy_x, enemy_y])

    # Self and other will swap a random child node
    def cross(self, other):
        n1 = random.choice(self.root.getNodes())
        n2 = random.choice(other.root.getNodes())
        n1.swap(random.choice(n1.children), random.choice(n2.children), n2)

    def set_mutation_rate(self, rate):
        pass  # The mutation rate does not change for the Decision_Tree_Genetic

    def mutate1(self):
        self.root.adjust(recursive=True)
        return self

    def mutate2(self):
        n = random.choice(self.root.getNodes())
        n.remove(random.choice(n.children))

        n = random.choice(self.root.getNodes())
        new_node = random.randrange(-1, 2)
        i = random.randrange(0, 7)
        if i != n.index:
            new_node = self.Node(i, random.randrange(-1, 2))
            new_node.add(random.randrange(-1, 2))
        n.add(new_node)
        return self
