from Wezen import Creature

class Monster(Creature):

    def __init__(self, name, hp=100, ap=20):
        self.name = name
        self.hp = hp
        self.ap = ap