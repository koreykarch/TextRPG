import time
import Enemy
import random
import Weapon
import Armor


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 25
        self.hit = 85
        self.crit = 15
        self.gold = 0
        self.potions = 0
        # define the player's starter weapon
        self.weapon = Weapon.Weapon("Wooden Stick", 0, 5, "\"A sturdy wooden stick...doesn't seem too useful.\"")
        self.armor = Armor.Armor("Cloth Armor", 0, 5, "\"Simple outfit from home...doesn't offer much protection.... \"")

    def heal(self):
        if self.getPotions() <= 0:
            print("No potions")
        else:
            if self.health == 100:
                print("You are already at maximum health...")
            else:
                self.health = self.health + 50
                if self.health > 100:
                    self.health = 100
                print("You are now at", self.getHealth(), "health")
                self.setPotions(self.getPotions() - 1)

    def inspect(self, obj):
        print(obj.getName(), "is a(n)", obj.getFaction())

    def attack(self, obj):
        print("You swing...")
        time.sleep(1)
        dmg = self.getAttack_power() + self.weapon.getDamage()
        hit_chance = random.randint(1,100)
        crit_chance = random.randint(1,100)
        if hit_chance > self.getHit():
            print("Attack missed...")
            print(obj.getName(), "has", obj.getHealth(), "health remaining\n")
        else:
            if crit_chance < self.getCrit():
                dmg = dmg * 1.5
                print("Critical hit!")
            obj.setHealth(obj.getHealth() - dmg)
            print("You hit", obj.getName(),"for", dmg)
            if obj.getHealth() > 0:
                print(obj.getName(), "has", obj.getHealth(), "health remaining\n")
            elif obj.getHealth() <= 0:
                print(obj.getName(), " has been killed")
                self.gold += obj.getGold_value()
                print(obj.getGold_value(), "gold looted!\n")

    def getHealth(self):
        return self.health

    def getAttack_power(self):
        return self.attack_power

    def setAttack_power(self, num):
        self.attack_power = num

    def setHealth(self, num):
        self.health = num

    def isAlive(self):
        return self.getHealth() > 0

    def setCrit(self, num):
        self.crit = num
    def setHit(self, num):
        self.hit = num
    def getCrit(self):
        return self.crit
    def getHit(self):
        return self.hit
    def getGold(self):
        return self.gold
    def setGold(self, num):
        self.gold = num
    def getPotions(self):
        return self.potions
    def setPotions(self, num):
        self.potions = num
    def setWeapon(self, wep):
        self.weapon = wep
    def setArmor(self, armor):
        self.armor = armor

