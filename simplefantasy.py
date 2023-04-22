import random

# player's character class
class Player:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

# monster class
class Monster:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

# function to calculate damage dealt
def calculate_damage(attacker, defender):
    return attacker.attack - defender.defense

# create player character
player = Player("Player", 100, 30, 10)

# create monsters
goblin = Monster("Goblin", 50, 20, 5)
troll = Monster("Troll", 80, 25, 15)
dragon = Monster("Dragon", 200, 50, 30)

# list of monsters
monsters = [goblin, troll, dragon]

# game loop
while True:
    # print player's current status
    print("Name: ", player.name)
    print("HP: ", player.hp)
    print("Attack: ", player.attack)
    print("Defense: ", player.defense)
    print("\n")
    # print options
    print("What would you like to do?")
    print("1. Explore the world")
    print("2. Check inventory")
    print("3. Exit game")
    choice = input("Enter your choice: ")
    if choice == "1":
        # randomly encounter a monster
        monster = random.choice(monsters)
        print("You have encountered a ", monster.name)
        # player chooses to fight or run
        fight_or_run = input("Do you want to fight or run? ")
        if fight_or_run == "fight":
            while monster.hp > 0 and player.hp > 0:
                print("You attack the ", monster.name)
                damage = calculate_damage(player, monster)
                monster.hp -= damage
                print("You dealt ", damage, " damage to the ", monster.name)
                print("The ", monster.name, " has ", monster.hp, " HP left")
                if monster.hp <= 0:
                    print("You have defeated the ", monster.name)
                    break
                print("The ", monster.name, " attacks you.")
                damage = calculate_damage(monster, player)
                player.hp -= damage
                print("The ", monster.name, " dealt ", damage, " damage to you.")
                print("You have ", player.hp, " HP left.")
        elif fight_or_run == "run":
            print("You successfully ran away.")
    elif choice == "2":
        # check inventory
        pass
    elif choice == "3":
        print("Thank you for playing.")
        break

#Hi Manya