import Enemy

class Dragon(Enemy.Enemy):
    def __init__(self):
        super().__init__('Dragon', 120, 45)
        self.gold_value = 200

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print(f"{self.getName()}: \"ROOOOOOAAAAAAR\"")