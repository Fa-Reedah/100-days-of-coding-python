# Updated BMI
'''
height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))
'''
BMI = 18.5   # round(weight/(height**2))
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are Overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are Obese")
else:
    print(f"Your BMI is {BMI}, you are Clinically Obese")
