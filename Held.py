from Wezen import Creature

class Hero(Creature):
    
    def __init__(self, name, hp=1000, ap=30):
        self.name = name
        self.hp = hp
        self.ap = hp