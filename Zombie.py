import Enemy
class Zombie(Enemy.Enemy):
    def __init__(self):
        super().__init__('Zombie', 50, 10)
        self.gold_value = 50

    def getGold_value(self):
        return self.gold_value

    def taunt(self):
        print(f"{self.getName()} \"Braaaaains\" ")