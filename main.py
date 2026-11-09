# Dette er egentlig ikke en del av oppgaven
# Men nå får vi teste om det fungerer

# Vi har ikke battle class enda så har ikke lagt det til
from character_class_4 import Character, Warrior, Mage
from items import Weapon
from dice_class import Dice
import random

print("Welcome to this RPG battle simulator!")

# Choose character name
name = input("Enter your character's name: ")

print(f"Which subclass will {name} be? Your options are:")
print("1: Warrior. A defensive specialist with an advantage against attack rolls.")
print("2: Mage. A resource-based attacker able to deal a magical spell for double attack damage.")

subclass_choice = input("Your choice (1/2):")

if subclass_choice == "1":
    hero = Warrior(name)
elif subclass_choice == "2":
    hero = Mage(name)

# Choose weapon
print("Choose your weapon:")
print("1. Greatsword. d12 damage.")
print("2: Bow. d6 damage.")
print("3: No weapon - use your character's default damage")

weapon_choice = input("Your choice (1/2/3): ")

if weapon_choice == "1":
    weapon = Weapon("Greatsword", Dice(20))
elif weapon_choice == "2":
    weapon = Weapon("Bow", Dice(6))
else:
    weapon = None
 
# Some enemy options
enemies = [
    Character("Goblin", hp_max=50, damage=8),
    Warrior("Orc", hp_max=100, damage=15, armor=3),
    Mage("Dark Wizard", hp_max=60, damage=12)
]

enemy = random.choice(enemies)

# Test
print(hero)
print(f"Your enemy is {enemy}")