import Enemy

class Wolf(Enemy.Enemy):
    def __init__(self):
        super().__init__('Wolf', 65, 15)
        self.gold_value = 25

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print(f"{self.getName()}: \"Grrrr.....\" ")