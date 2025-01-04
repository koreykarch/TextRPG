import Enemy

class Goblin(Enemy.Enemy):
    def __init__(self):
        super().__init__('Goblin', 70, 30)
        self.gold_value = 125

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print(f"{self.getName()}: \"Time is money, friend!\"")