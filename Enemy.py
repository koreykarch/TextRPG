import Player
import time
import sys
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.faction = "Enemy"

    def heal(self, amount):
        if self.health == 100:
            print("You are already at maximum health...")
        else:
            self.health += amount
            if self.health > 100:
                self.health = 100

    def attack(self, player):
        """Perform an attack on the player."""
        if not self.isAlive():
            return  # No attack if dead
        print(f"{self.name} attacks!")
        time.sleep(1)

        # Simple damage calculation
        damage_dealt = self.attack_power - player.armor.getProtection()
        if damage_dealt < 0:
            damage_dealt = 0  # negative damage doesn't make sense

        player.setHealth(player.getHealth() - damage_dealt)
        print(f"{self.name} hits you for {damage_dealt} damage.")
        print(f"You have {player.getHealth()} health left.\n")


    def getHealth(self):
        return self.health
    def getMax_health(self):
        return self.max_health

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
    
    def printStats(self):
        print(f"{self.name}: {self.max_health} max health, {self.attack_power} attack power")




