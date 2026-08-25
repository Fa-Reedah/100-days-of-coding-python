# Tip Calculator

print("Welcome to the Tip Calculator.")
bill = round(float(input("What was the total bill? #")), 2)
percent = round(float(input("What percentage tip would you like to give?10, 12 or 15? #")), 2)
num_of_split = round(float(input("How many people to split the bill? ")), 2)

result = round((bill + (percent/100) * bill) / num_of_split, 2)
result = "{:.2f}".format(result)     # take note
print(f"Each person should pay # {result}")
