# Rock, Paper, Scissors

import random

rock = "👊"
paper = "🤚"
scissors = "✌️"

list_all = [rock, paper, scissors]

user_input = input("Choose one, R=👊, P=🤚, S=✌️ \n ")
new_user_input = user_input.lower()
if new_user_input == "r":
    user = "👊"
    print(f"User chose {user}")
elif new_user_input == "p":
    user = "🤚"
    print(f"User chose {user}")
elif new_user_input == "s":
    user = "✌️"
    print(f"User chose {user}")
else:
    print("Invalid Input")

comp_rand = random.choice(list_all)
print(f"Computer chose {comp_rand}")

if user == comp_rand:
    print("Draw")
elif (user == "👊" and comp_rand == "✌️") or (user == "✌️" and comp_rand == "🤚") or (user == "🤚" and comp_rand == "👊"):
    print("User Wins")
else:
    print("Computer Wins")
