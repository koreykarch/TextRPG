import Enemy

class Bandit(Enemy.Enemy):
    def __init__(self):
        super().__init__('Bandit', 80, 20)
        self.gold_value = 75

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print("Bandit: \"Give me your gold or die!\" ")