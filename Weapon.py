class Weapon:
    def __init__(self, name, cost, damage, description):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.description = description

    def setName(self, name):
        self.name = name

    def setCost(self, cost):
        self.cost = cost

    def setDamage(self, damage):
        self.damage = damage

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getDamage(self):
        return self.damage

    def getDescription(self):
        return self.description

    def setDescription(self, string):
        self.description = string

    def shopDesc(self):
        print(self.name + " - Damage:" , self.damage,"| Cost:", self.cost, "gold |", self.getDescription())
