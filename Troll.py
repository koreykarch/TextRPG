import Enemy

class Troll(Enemy.Enemy):
    def __init__(self):
        super().__init__('Troll', 115, 20)
        self.gold_value = 120

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print(f"{self.getName()}: \"You die now!!\"")