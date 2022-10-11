import Player
import time
import sys
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.faction = "Enemy"
        self.aliveStatus = True

    def heal(self, num):
        if self.health == 100:
            print("You are already at maximum health...")
        else:
            self.health = self.health + num
            if self.health > 100:
                self.health = 100

    def attack(self, obj):
        if self.getHealth() <= 0:
            pass
        else:
            print(self.getName(), "attacks you...")
            time.sleep(1)
            obj.setHealth((obj.getHealth() - self.getAttack_power()) + obj.armor.getProtection())
            print(self.getName(), "hits you for", self.getAttack_power() - obj.armor.getProtection())
            print("You have", obj.getHealth(), "health remaining\n")
            if obj.getHealth() <= 0:
                print("You have been killed and lost", obj.getGold() / 2, "gold")
                obj.setGold(obj.getGold() / 2)

    def getHealth(self):
        return self.health

    def getAttack_power(self):
        return self.attack_power

    def setAttack_power(self, num):
        self.attack_power = num

    def setHealth(self, num):
        self.health = num

    def getFaction(self):
        return self.faction
    def getName(self):
        return self.name
    def isAlive(self):
        return self.getHealth() > 0




