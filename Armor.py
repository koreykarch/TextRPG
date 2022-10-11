class Armor:
    def __init__(self, name, cost, protection, description):
        self.name = name
        self.cost = cost
        self.protection = protection
        self.description = description

    def setName(self, name):
        self.name = name

    def setCost(self, cost):
        self.cost = cost

    def setProtection(self, prot):
        self.protection = prot

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getProtection(self):
        return self.protection

    def getDescription(self):
        return self.description

    def setDescription(self, string):
        self.description = string

    def shopDesc(self):
        print(self.name + " - Blocks" , self.protection,"damage| Cost:", self.cost, "gold |", self.getDescription())
