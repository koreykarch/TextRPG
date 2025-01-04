from data.levels import LEVEL_DATA, LEVEL_CONNECTIONS
from data.enemies import ENEMY_CLASSES
from Level import Level
from Player import Player
import Armor
import Weapon
import random
import time

# obj list to store the weapon objects for the shop
shop_weapons = [
    Weapon.Weapon("Dagger", 100, 5, "A small, sharp dagger"),
    Weapon.Weapon("Wooden Club", 250, 15, "A heavy wooden club"),
    Weapon.Weapon("Iron Sword", 500, 25, "A sharp sword made of iron"),
    Weapon.Weapon("Katana", 1000, 50, "An extremely sharp katana"),
    Weapon.Weapon("Samurai Sword", 1250, 75, "A legendary samurai sword")

]
shop_armor = [
    Armor.Armor("Leather Armor", 350, 10, "Armor made from animal skin"),
    Armor.Armor("Chainmail Armor", 1000, 20, "Armor made from chainmail"),
    Armor.Armor("Plate Armor", 2000, 40, "Heavy plate armor"),
]


def viewInventory(player):
    print("\n" + "=" * 50)
    print("         I N V E N T O R Y")
    print("=" * 50)
    print(f"Gold: {player.getGold()}")
    print(f"Potions: {player.getPotions()}")
    print(f"Health: {player.getHealth()}")
    print()
    print(f"Weapon: {player.weapon.getName()} (+{player.weapon.getDamage()} dmg) | {player.weapon.getDescription()}")
    print(f"Armor:  {player.armor.getName()} (+{player.armor.getProtection()} block) | {player.armor.getDescription()}")
    print("=" * 50)
    while True:
        try:
            print("\n[0] Exit Inventory")
            print("[1] Use a potion to heal")
            inv_op = int(input("Choice: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if inv_op < 0 or inv_op > 1:
            print("Invalid choice.")
        else:
            break
    if inv_op == 1:
        player.heal()
    # end of function
    print("=" * 50 + "\n")



def fight_sequence(player, level_obj):
    enemy = level_obj.getRandomEnemy(ENEMY_CLASSES)
    
    print("\n" + "=" * 50)
    print("             F I G H T !")
    print("=" * 50)
    print(f"You encounter a {enemy.getName()} with {enemy.getHealth()} health!")
    enemy.taunt()
    print("=" * 50 + "\n")
    time.sleep(1)

    # main fight loop
    while enemy.isAlive() and player.isAlive():
        print(f"Your Health: {player.getHealth():.0f}")
        print(f"Enemy Health: {enemy.getHealth():.0f}/{enemy.getMax_health()}")
        print()
        print("[1] Attack")
        print(f"[2] Use Potion ({player.getPotions()} left)")
        print(f"[3] Inspect {enemy.getName()}")
        
        try:
            fight_choice = int(input("Choice: "))
        except ValueError:
            print("\nInvalid choice.\n")
            continue
        
        print()  # blank line

        if fight_choice == 1:
            # Player attacks
            player.attack(enemy)
            print()
            time.sleep(0.8)
        elif fight_choice == 2:
            player.heal()
            print()
            time.sleep(0.8)
        elif fight_choice == 3:
            enemy.printStats()
            print()
            continue
        else:
            print("Invalid choice.\n")
            continue
        
        # Enemy's turn (if still alive)
        if enemy.isAlive():
            enemy.attack(player)
            print()
            time.sleep(1)

    # After fight ends
    if not player.isAlive():
        print("You have fallen in battle...")
        print("You have been killed and lost", player.getGold() / 2, "gold")
        player.setGold(player.getGold() / 2)
    else:
        print(f"You have defeated the {enemy.getName()}!\n")
    print("=" * 50 + "\n")
    time.sleep(1)

def shop_logic(player):
    while True:
        print("\n--- Welcome to the Shop! ---")
        print(f"You have {player.getGold()} gold.")
        print(f"Health: {player.getHealth()}")
        print("[1] Buy a potion (100 gold)")
        print("[2] View weapons for sale")
        print("[3] View armor for sale")
        print("[0] Return to city")
        choice = input("Choice: ")
        
        if choice == "0":
            break
        elif choice == "1":
            if player.getGold() >= 100:
                player.setGold(player.getGold() - 100)
                player.setPotions(player.getPotions() + 1)
                print("Potion purchased!")
            else:
                print("Not enough gold for a potion.")
        elif choice == "2":
            # Show weapons
            for i, w in enumerate(shop_weapons, start=1):
                print(f"[{i}] {w.getName()} - Cost: {w.getCost()} - Damage: {w.getDamage()}")
            print("[0] Go Back")
            buy_choice = int(input("Choice: "))
            if buy_choice == 0:
                pass
            elif 1 <= buy_choice <= len(shop_weapons):
                chosen_weapon = shop_weapons[buy_choice - 1]
                if player.getGold() < chosen_weapon.getCost():
                    print("Not enough gold.")
                else:
                    # Maybe check if the new weapon is "better"
                    player.setGold(player.getGold() - chosen_weapon.getCost())
                    player.setWeapon(chosen_weapon)
                    print("Weapon purchased!")
        elif choice == "3":
            # Show armors
            for i, a in enumerate(shop_armor, start=1):
                print(f"[{i}] {a.getName()} - Cost: {a.getCost()} - Protection: {a.getProtection()}")
            print("[0] Go Back")
            buy_choice = int(input("Choice: "))
            if buy_choice == 0:
                pass
            elif 1 <= buy_choice <= len(shop_armor):
                chosen_armor = shop_armor[buy_choice - 1]
                if player.getGold() < chosen_armor.getCost():
                    print("Not enough gold.")
                else:
                    player.setGold(player.getGold() - chosen_armor.getCost())
                    player.setArmor(chosen_armor)
                    print("Armor purchased!")
        else:
            print("Invalid choice.")

def roulette_logic(player):
    print("\n\n________________\nWelcome to Roulette")
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    while True:
        print("You have", player.getGold(), "gold")
        player_wagers = []
        total_wager = 0
        amt = 0
        bet_color = int(input("Bet black [1], Red [2], Neither [0], Exit [99]"))
        if bet_color == 99:
            break
        if bet_color == 1:
            print("How much to bet on black?")
            amt = int(input())
            if amt > player.getGold():
                print("You don't have the gold for that...")
                continue
            else:
                print("You have" ,player.getGold() - amt, "gold left to bet")
        if bet_color == 2:
            print("How much to bet on red?")
            amt = int(input())
            if amt > player.getGold():
                print("You don't have the gold for that...")
                break
            else:
                print("You have", player.getGold() - amt, "gold left to bet")
        print("How much gold would you like to wager per spot? ([99] to exit)")
        wager = int(input())
        if wager == 99:
            break
        if wager > player.getGold():
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
                elif (total_wager + wager + amt) > player.getGold():
                    print("You don't have enough gold to make this bet \n[99] to finish betting")
                else:
                    if xr in player_wagers:
                        print("You have already bet this number")
                    else:
                        player_wagers.append(xr)
                        print("Bet", wager, "gold on", xr)
                        count = count + 1
                        total_wager = wager * count
            player.setGold(player.getGold() - (total_wager + amt))
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
                    player.setGold(player.getGold() + (amt * 2))
                if bet_color == 1:
                    print("You lost", amt, "gold on black")
            elif win_num in black_numbers:
                print("Black number)")
                if bet_color == 1:
                    print("You won", amt, "gold on black!")
                    player.setGold(player.getGold() + (amt * 2))
                if bet_color == 2:
                    print("You lost", amt, "gold on red!")
            else:
                print("Green number)")
            if win_num in player_wagers:
                print("You won", (wager * 35) - wager, "gold on", win_num)
                print("")
                player.setGold(player.getGold() + (wager * 35))
            else:
                print("You didn't bet this number")
                print("You lost", total_wager, "gold on your numbers")
                print("")
 
def main():
    player = Player("Player")
    player.setGold(50000)  # for testing

    # Create a dictionary of Level objects from LEVEL_DATA
    levels = {}
    for level_name, data in LEVEL_DATA.items():
        levels[level_name] = Level(
            name=level_name,
            description=data["description"],
            enemy_names=data["enemies"]
        )

    current_location = "city"

    while True:
        # If dead, restore health
        if not player.isAlive():
            player.setHealth(100)
            current_location = "city"

        # 1. Describe current location
        current_level_obj = levels[current_location]
        current_level_obj.describe()
        
        # 2. Check if this is a “combat zone” by seeing if it has enemies
        if current_level_obj.enemy_names:
            print(f"Health: {player.getHealth()}")
            # Let the player choose to fight or not
            print("[1] Fight an enemy")
            print("[2] View inventory")
            print("[3] Go somewhere else")
            choice = input("Choice: ")

            if choice == "1":
                fight_sequence(player, current_level_obj)
                continue  # then re-describe, re-offer fight as long as we stay here
            elif choice == "2":
                viewInventory(player)
                continue
            elif choice == "3":
                pass  # proceed to traveling
            else:
                print("Invalid choice.")
                continue
        else:
            # For "city," "shop," or "roulette," do special logic
            if current_location == "shop":
                shop_logic(player)
                # after returning from shop, either stay or move
            elif current_location == "roulette":
                roulette_logic(player)
                # same idea: after roulette, either stay or move
            else:
                # city or any other non-combat zone
                print("[1] View inventory")
                print("[2] Go somewhere else")
                choice = input("Choice: ")

                if choice == "1":
                    viewInventory(player)
                    continue
                elif choice == "2":
                    pass
                else:
                    print("Invalid choice.")
                    continue

        # 3. Show possible neighbors for current_location
        neighbors = LEVEL_CONNECTIONS[current_location]
        if not neighbors:
            print("There are no exits from here!")
            break  # or do something else

        print("\nWhere would you like to go next?")
        for i, loc in enumerate(neighbors, start=1):
            print(f"[{i}] {loc}")
        print("")
        print("[99] Cancel")
        print("[0] Quit Game")
        move_choice = input("Choice: ")

        if move_choice == "0":
            print("Goodbye!")
            break
        elif move_choice.isdigit():
            move_choice = int(move_choice)
            if move_choice == 99:
                pass
            if 1 <= move_choice <= len(neighbors):
                current_location = neighbors[move_choice - 1]
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()