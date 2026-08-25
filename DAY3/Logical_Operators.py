# Logical Operators

# AND Operators
a = 5
b = 8
print(a > 6 and b < 2)
print(a > 3 and b > 5)


# OR Operators
a = 5
b = 8
print(a > 6 or b < 2)
print(a > 3 or b > 5)

# NOT Operators
a = 5
b = 8
print(not a > 15)


# Rollercoaster with Midlife Crisis

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age?"))

    if age <= 12:
        bill = 5
        print("Child tickets are #5")

    elif age <= 18:
        bill = 7
        print("Teen tickets are #7")

    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is gonna be alright. Have a free ride on us!")

    else:
        bill = 12
        print("Adult tickets are #12")

    Pic = input("Do you want photos? Yes/No ")
    if Pic == "Yes":
        print(f"Total Bill is #{bill + 3}")

else:
    print("Sorry you have to grow taller to ride.")
