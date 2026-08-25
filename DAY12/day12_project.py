"""NUMBER GUESSING GAME"""
"""
import random

def rand_guess():
    Guess random number between 1 and 100
    rand_num = random.randint(1, 100)
    return rand_num


to_play = "y"
while to_play == "y":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    rand_num = rand_guess()
    #print(rand_num)

    
    attempts = 10
    while difficulty == "easy":
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        try:
            guess = int(input("Make a guess: "))
        except:        
            print("Invalid Input")
            continue
            
        if guess > rand_num:
            print("Too high. \nGuess again.")
        elif guess < rand_num:
            print("Too low. \nGuess again.")
        elif guess == rand_num:
            print(f"You got it; The answer is {rand_num}")
            difficulty = ""

        attempts -= 1
    
        if attempts == 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("You lose")
            difficulty = ""
            
    attempts = 5    
    while difficulty == "hard":
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        try:
            guess = int(input("Make a guess: "))
        except:        
            print("Invalid Input")
            continue 
    
        if guess > rand_num:
            print("Too high. \nGuess again.")
        elif guess < rand_num:
            print("Too low. \nGuess again.")
        elif guess == rand_num:
            print(f"You got it; The answer is {rand_num}")
            difficulty = ""

        attempts -= 1
        
        if attempts == 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            print("You lose")
            difficulty = ""
            
            
    if not difficulty == "easy" and not difficulty == "hard" and not difficulty == "":
        print("Invalid input")
        
    to_play = str(input("Would you like to play again? Type 'y' for Yes or Type 'n' for No: ")).lower()
    
    while not to_play == "y" and not to_play == "n":
        print("Invalid input")
        to_play = str(input("Would you like to play again? Type 'y' for Yes or Type 'n' for No: ")).lower()
    
if to_play == "n":
    print("END")
    


def mutate(a_list):
    #mutate
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

"""


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
