# AI-Snake-Duel
# David Bonsant
# Jérémie Beaudoin-Dion

# Ce fichier est l'objet de base pour un joueur
class Player:
    def __init__(self, index, x, y, width, length, age=5):
        self.index = index
        self.x = x
        self.y = y
        self.width=width
        self.length=length
        self.age = age

    def update(self):
        self.move()

    def move(self):
        # moving logic
        self.x-=-1
        # wrap around
        self.x %= self.width
        self.y %= self.length

    def die(self):
        pass
