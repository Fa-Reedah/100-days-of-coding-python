print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Small_pizza = 15
Medium_pizza = 20
Large_pizza = 25

Pepperoni_4_Smalls = 2
Pepperoni_4_Medium_Large = 3
extra_cheese_4_all = 1
bill = 0

if size == "S":
    bill = Small_pizza
elif size == "M":
    bill = Medium_pizza
else:
    bill = Large_pizza

if add_pepperoni == "Y":
    if size == "S":
        bill = Small_pizza + Pepperoni_4_Smalls
    elif size == "M":
        bill = Medium_pizza + Pepperoni_4_Medium_Large
    elif size == "L":
        bill = Large_pizza + Pepperoni_4_Medium_Large

if extra_cheese == "Y":
    bill += 1
print(f"Your Bill is #{bill}")
