# Who's Paying: Banker Roulette
import random

name_string = input("Give me everybody's names, seperated by a comma. ").split(", ")
num_name = len(name_string)

rand_name = random.randint(0, num_name-1)

print(f"{name_string[rand_name]} is buying the meal today!")


rand_name = random.choice(name_string)
print(rand_name)
