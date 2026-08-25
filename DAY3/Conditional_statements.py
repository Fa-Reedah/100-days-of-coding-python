# If/else
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height >= 120:  # (<,>,<=,>=,==,!=)
    print("You can ride the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride.")


# Exercise.
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# if/elif/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  # (<,>,<=,>=,==,!=)
    print("You can ride the rollercoaster!")

    age = int(input("What is your age?"))
    if age < 12:

        Pic = print(input("Do you want photos? Yes/No"))

        if Pic == "Yes":
            print(f"Total Bill is #{5 + 3}")
        else:
            print(f"Total Bill is #{5}")

    if age <= 18:

        Pic = print(input("Do you want photos? Yes/No"))

        if Pic == "Yes":
            print(f"Total Bill is #{7 + 3}")
        else:
            print(f"Total Bill is #{7 + 3}")

    else:
        Pic = print(input("Do you want photos? Yes/No"))
        if Pic == "Yes":
            print(f"Total Bill is #{12 + 3}")
        else:
            print(f"Total Bill is #{12}")
else:
    print("Sorry you have to grow taller before you can ride.")
'''
# ROLLER COASTER
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

    else:
        bill = 12
        print("Adult tickets are #12")

    Pic = input("Do you want photos? Yes/No ")
    if Pic == "Yes":
        print(f"Total Bill is #{bill + 3}")

else:
    print("Sorry you have to grow taller to ride.")
