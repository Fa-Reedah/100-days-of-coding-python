# Rounding up
'''
print(round(8 / 3))
print(round(8 / 3, 3))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print(score)
'''

score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, Your height is {height}, Winning (True/False)?{isWinning}")


# Exercise

# Get Current Age
age = input("What is your current age?")
# Calc Age left
age_left_in_Years = 90 - int(age)
# Conv Age left to Days, Weeks, Months
age_left_in_Months = age_left_in_Years * 12
age_left_in_Weeks = age_left_in_Years * 52
age_left_in_Days = age_left_in_Years * 365
# Print Output
print(f"You have {age_left_in_Days} days, {age_left_in_Weeks} weeks, and {age_left_in_Months} months left")