# Leap year. Difficult

Year = int(input("Input Year"))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("It is a Leap Year!")
    else:
        print("It is a Leap Year!")
else:
    print("It is not a Leap Year!")
