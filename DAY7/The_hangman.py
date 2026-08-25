# HANGMAN CHALLENGE
import random
import hang_ASCII
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(chosen_word)
print(f"Psssst, the solution is {chosen_word}")

display = []

for L in chosen_word:
    display += "_"
print(display)
lives = 6

while "_" in display:

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        position = 0
        for p in chosen_word:
            position += 1
            if guess == p:
                display[position - 1] = guess
        print(display)
    else:
        lives -= 1
        print(f"Wrong!\n You have {lives} lives left")
        if lives == 0:
            print("GAME OVER")
            display = []
        else:
            print(display)
