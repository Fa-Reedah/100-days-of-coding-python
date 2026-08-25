"""LAST BEGINNER PROJECT"""
import random
import os
from ascii_art import higher_lower_logo, vs_logo


Rnd1 = [
    {"name": "Cristiano Ronaldo", "job": "Footballer", "country": "Portugal", "followers": "640"},
    {"name": "Lionel Messi", "job": "Footballer", "country": "Argentina", "followers": "510"},
    ]

celebrities = [
    {"name": "Selena Gomez", "job": "Singer and actress", "country": "United States", "followers": "425"},
    {"name": "Kylie Jenner", "job": "Entreprenuer/Media", "country": "United States", "followers": "400"},
    {"name": "Dwayne Johnson", "job": "Actor", "country": "United States", "followers": "395"},
    {"name": "Ariana Grande", "job": "Singer", "country": "United States", "followers": "380"},
    {"name": "Kim Kardashian", "job": "Entreprenuer/Media", "country": "United States", "followers": "360"},
    {"name": "Beyonce", "job": "Singer", "country": "United States", "followers": "320"},
    {"name": "Khloe Kardashian", "job": "Entreprenuer/Media", "country": "United States", "followers": "310"},
    {"name": "Nicki Minaj", "job": "Rapper", "country": "United States", "followers": "230"}
    ]


def clear_screen():
    """clear screen"""
    os.system("cls")


def rand_choice():
    """computer shuffles and pop the last celebrity in list"""
    random.shuffle(celebrities)
    picked = celebrities.pop()
    return picked


def check_answer():

    ans_ = None
    if picked1['followers'] > picked2[-1]['followers']:
        ans_ = 'b'
    elif picked2[-1]['followers'] > picked1['followers']:
        ans_ = 'a'

    return ans_


print(higher_lower_logo)

score = 0
picked2 = []

print(f"Compare A: {Rnd1[0]['name']}, a {Rnd1[0]['job']}, from {Rnd1[0]['country']}")

print(vs_logo)

print(f"Against B: {Rnd1[1]['name']}, a {Rnd1[1]['job']}, from {Rnd1[1]['country']}")
picked2.append(Rnd1[1])

user_ans = str(input("Who has more followers. Type 'A' or 'B': ")).lower()

ans = 'a'
if user_ans == ans:
    score += 1
    result = f"You're right! Current score: {score}"
else:
    result = f"You're wrong. Current score: {score}"

print(result)

clear_screen()

while user_ans == ans:
    print(higher_lower_logo)
    print(result)
    picked1 = rand_choice()
    rand_celeb = f"{picked1['name']}, a {picked1['job']}, from {picked1['country']}."
    prev_celeb = f"{picked2[-1]['name']}, a {picked2[-1]['job']}, from {picked2[-1]['country']}."

    print(f"Compare A: {prev_celeb}")

    print(vs_logo)

    print(f"Against B: {rand_celeb}")
    user_ans = str(input("Who has more followers. Type 'A' or 'B': ")).lower()
    ans = check_answer()

    while user_ans != 'a' and user_ans != 'b':
        print("Invalid input")
        user_ans = str(input("Who has more followers. Type 'A' or 'B': "))

    clear_screen()

    if user_ans == ans:
        score += 1
        result = f"You're right! Current score: {score}"
    else:
        result = f"You're wrong. Final score: {score}"
        print(higher_lower_logo)
        print(result)

    picked2.append(picked1)

    if len(celebrities) == 0:
        ans = ()
        print(higher_lower_logo)
        print(f"END. \nYour final score is {score}")
