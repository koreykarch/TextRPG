class Level:
    def __init__(self, name, description, enemy_names):
        self.name = name
        self.description = description
        self.enemy_names = enemy_names  # just the string names

    def getRandomEnemy(self, enemy_classes):
        import random
        from data.enemies import ENEMY_CLASSES
        enemy_name = random.choice(self.enemy_names)
        enemy_class = enemy_classes[enemy_name] 
        return enemy_class()

    def describe(self):
        print(f"--- {self.name.upper()} ---")
        print(self.description)
