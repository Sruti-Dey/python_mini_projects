import random

health =50
difficulty=3
h_potion=int(random.randint(25,50)/difficulty)
health = health +h_potion
print("Your current health is -",health)
