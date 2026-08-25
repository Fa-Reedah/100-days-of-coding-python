# LOVE CALCULATOR
print("Welcome to love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined = (name1 + name2).lower()
true = sum(combined.count(letter) for letter in "true")
love = sum(combined.count(letter) for letter in "love")
x = int(str(true) + str(love))
print(x)

if x < 10 or x > 90:
    print(f"Your Score is {x}, you go together like coke and mentos")
elif x >= 40 and x <= 50:
    print(f"Your Score is {x}, you are alright together")
else:
    print(f"Your Score is {x}")
