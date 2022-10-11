import Goblin
import Armor
import Player
import Zombie
import Weapon
import Wolf
import random
import Bandit
import time

P1 = Player.Player("Player")
# # TEMPORARY ASSERTION
P1.setGold(500)

# obj list to store the weapon objects for the shop
shop_weapons = []
wooden_club = Weapon.Weapon("Wooden Club", 250, 15, "A heavy wooden club")
iron_sword = Weapon.Weapon("Iron Sword", 500, 25, "A sharp sword made of iron")
katana_sword = Weapon.Weapon("Katana", 1000, 50, "An extremely sharp katana")

shop_weapons.append(wooden_club)
shop_weapons.append(iron_sword)
shop_weapons.append(katana_sword)

shop_armor = []
leather_armor = Armor.Armor("Leather Armor", 350, 10, "Armor made from animal skin")
chainmail_armor = Armor.Armor("Chainmail Armor", 1000, 20, "Armor made from chainmail")

shop_armor.append(leather_armor)
shop_armor.append(chainmail_armor)

currentLevel = " "

def viewInventory(obj):
    print("________________________")
    print("You have", obj.getGold(), "gold")
    print("You have", obj.getPotions(), "potions")
    print("Your current weapon is a", obj.weapon.getName(), "(+", obj.weapon.getDamage(), "damage)", "|",
          obj.weapon.getDescription())
    print("Your current armor is", obj.armor.getName(), "(+", obj.armor.getProtection(), "block)", "|", obj.armor.getDescription())
    while True:
        try:
            print("Press 0 to exit inventory, or 1 to heal with a potion")
            inv_op = int(input())
        except ValueError:
            print("Invalid choice")
            continue
        if inv_op < 0 or inv_op > 3:
            print("Invalid choice")
        else:
            break
    if inv_op == 1:
        obj.heal()
    elif inv_op == 0:
        pass
    print("_________________________________________")

def fightSequence(level):
    enemy_list = []
    if level == "forest":
        Z = Zombie.Zombie()
        W1 = Wolf.Wolf()
        enemy_list.append(Z)
        enemy_list.append(W1)
    elif level == "dark_forest":
        B = Bandit.Bandit()
        G = Goblin.Goblin()
        enemy_list.append(B)
        enemy_list.append(G)
    x = random.randrange(0, len(enemy_list))
    print("Fighting a", enemy_list[x].getName(), "with", enemy_list[x].getHealth(), "health")
    enemy_list[x].taunt()
    while enemy_list[x].isAlive() and P1.isAlive():
        while True:
            try:
                print("1. Attack")
                print("2. Use Potion (", P1.getPotions(), "potions left )")
                fight_choice = int(input())
            except ValueError:
                print("Invalid choice")
                # better try again... Return to the start of the loop
                continue
            if fight_choice > 2 or fight_choice < 1:
                print("Invalid Choice")
                continue
            else:
                break
        if fight_choice == 1:
            P1.attack(enemy_list[x])
        elif fight_choice == 2:
            P1.heal()
        else:
            print("invalid choice")
        enemy_list[x].attack(P1)


# main game loop
while True:
    # check if player is "coming back" from being dead. if so, reset health to 100
    if not P1.isAlive():
        P1.setHealth(100)
    print("__________________")
    currentLevel = "city"
    choice = int(input("Press 1 to enter the Forest\nPress 2 to visit the shop\nPress 3 to view inventory\nPress 4 to Play Roulette"))
    if choice == 1:
        print("_______________________")
        print("You enter the Forest")
        while True and P1.isAlive():
            currentLevel = "forest"
            print("Player HP:", P1.getHealth())
            print("Press 1 to fight an enemy\nPress 2 to advance to the Dark Forest, 3 to view inventory, or 0 to turn back to the city")
            x = int(input())
            if x == 0:
                print("You head back into the city...")
                break
            elif x == 1:
                fightSequence(currentLevel)
            elif x == 2:
                print("___________________________")
                print("You enter the Dark Forest")
                while True and P1.isAlive():
                    currentLevel = "dark_forest"
                    print("Press 1 to fight an enemy or 3 to view inventory\nPress 0 to turn back to the Forest")
                    print("Player HP:", P1.getHealth())
                    x1 = int(input())
                    if x1 == 0:
                        print("You head back into the Forest...")
                        break
                    elif x1 == 1:
                        fightSequence(currentLevel)
                    elif x1 == 3:
                        viewInventory(P1)
            elif x == 3:
                viewInventory(P1)

    elif choice == 2:
        print("________________________")
        print("Welcome to the shop!")
        while(True):
            print("You have", P1.getGold(), "gold")
            print("Press [1] to buy a potion (100 gold)\npress [2] to view weapons for sale\nPress [3] to view Armor\nor [4] to exit\n")
            shopMenu_choice = int(input())
            if shopMenu_choice == 1:
                if P1.getGold() >= 100:
                    print("Potion purchased")
                    P1.setGold(P1.getGold() - 100)
                    P1.setPotions(P1.getPotions() + 1)
                else:
                    print("Not enough gold to purchase potion")
            elif shopMenu_choice == 2:
                while(True):
                    count = 0
                    for obj in shop_weapons:
                        print(count + 1, "- ", end="")
                        obj.shopDesc()
                        count += 1
                    print("Press 0 to return")
                    buy_weapon_choice = int(input())
                    # needs error handling in case user enters out of index bounds
                    if buy_weapon_choice == 0:
                        break
                    elif P1.getGold() < shop_weapons[buy_weapon_choice - 1].getCost():
                        print("You can't afford this item - ", shop_weapons[buy_weapon_choice - 1].getName())
                    elif P1.getGold() >= shop_weapons[buy_weapon_choice - 1].getCost():
                        if P1.weapon == shop_weapons[buy_weapon_choice - 1]:
                            print("You already own this weapon...")
                        elif P1.weapon.getDamage() > shop_weapons[buy_weapon_choice - 1].getDamage():
                            print("Why would you want this?")
                        else:
                            P1.setGold(P1.getGold() - shop_weapons[buy_weapon_choice - 1].getCost())
                            print("You have bought - ", shop_weapons[buy_weapon_choice - 1].getName())
                            print("You now have", P1.getGold(), "gold")
                            P1.setWeapon(shop_weapons[buy_weapon_choice - 1])
            elif shopMenu_choice == 3:
                while True:
                    a_count = 0
                    for obj in shop_armor:
                        print(a_count + 1, "- ", end="")
                        obj.shopDesc()
                        a_count += 1
                    print("Press 0 to return")
                    buy_armor_choice = int(input())
                    if buy_armor_choice == 0:
                        break
                    elif P1.getGold() < shop_armor[buy_armor_choice - 1].getCost():
                        print("You can't afford this item - ", shop_armor[buy_armor_choice - 1].getName())
                    elif P1.getGold() >= shop_armor[buy_armor_choice - 1].getCost():
                        if P1.armor == shop_armor[buy_armor_choice - 1]:
                            print("You already own this Armor...")
                        elif P1.armor.getProtection() > shop_armor[buy_armor_choice - 1].getProtection():
                            print("Why would you want this?")
                        else:
                            P1.setGold(P1.getGold() - shop_armor[buy_armor_choice - 1].getCost())
                            print("You have bought - ", shop_armor[buy_armor_choice - 1].getName())
                            print("You now have", P1.getGold(), "gold")
                            P1.setArmor(shop_armor[buy_armor_choice - 1])
            else:
                break
    elif choice == 3:
        viewInventory(P1)

    elif choice == 4:
        print("\n\n________________\nWelcome to Roulette")
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        while True:
            print("You have", P1.getGold(), "gold")
            player_wagers = []
            total_wager = 0
            amt = 0
            bet_color = int(input("Bet black [1], Red [2], Neither [0], Exit [99]"))
            if bet_color == 99:
                break
            if bet_color == 1:
                print("How much to bet on black?")
                amt = int(input())
                if amt > P1.getGold():
                    print("You don't have the gold for that...")
                    break
                else:
                    print("You have" ,P1.getGold() - amt, "gold left to bet")
            if bet_color == 2:
                print("How much to bet on red?")
                amt = int(input())
                if amt > P1.getGold():
                    print("You don't have the gold for that...")
                    break
                else:
                    print("You have", P1.getGold() - amt, "gold left to bet")
            print("How much gold would you like to wager per spot? ([99] to exit)")
            wager = int(input())
            if wager == 99:
                break
            if wager > P1.getGold():
                print("You do not have enough gold for that bet")
            else:
                print("Which spots would you like to wager? ([99] to finish betting)")
                count = 0
                while True:
                    xr = int(input())
                    if xr == 99:
                        break
                    elif xr < 0 or xr > 36:
                        print("You can't bet this number")
                    elif (total_wager + wager + amt) > P1.getGold():
                        print("You don't have enough gold to make this bet \n[99] to finish betting")
                    else:
                        if xr in player_wagers:
                            print("You have already bet this number")
                        else:
                            player_wagers.append(xr)
                            print("Bet", wager, "gold on", xr)
                            count = count + 1
                            total_wager = wager * count
                P1.setGold(P1.getGold() - (total_wager + amt))
                print("Numbers bet:\n___________")
                for i in player_wagers:
                    print(i)
                    time.sleep(.5)
                color = ""
                if bet_color == 2:
                    color = "red"
                elif bet_color == 1:
                    color = "black"
                print("Total wager:", total_wager + amt, "(", total_wager, "on numbers,", amt, "on color", color,")")
                win_num = random.randrange(0, 37)
                print("Spinning...")
                time.sleep(3)
                print("\n\n\n_______________________________\nWinning number:", win_num, end=" (")
                if win_num in red_numbers:
                    print("Red number)")
                    if bet_color == 2:
                        print("You won", amt, "gold on red!")
                        P1.setGold(P1.getGold() + (amt * 2))
                    if bet_color == 1:
                        print("You lost", amt, "gold on black")
                elif win_num in black_numbers:
                    print("Black number)")
                    if bet_color == 1:
                        print("You won", amt, "gold on black!")
                        P1.setGold(P1.getGold() + (amt * 2))
                    if bet_color == 2:
                        print("You lost", amt, "gold on red!")
                else:
                    print("Green number)")
                if win_num in player_wagers:
                    print("You won", (wager * 35) - wager, "gold on", win_num)
                    print("")
                    P1.setGold(P1.getGold() + (wager * 35))
                else:
                    print("You didn't bet this number")
                    print("You lost", total_wager, "gold on your numbers")
                    print("")

