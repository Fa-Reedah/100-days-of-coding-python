"""COFFEE MACHINE"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    "cost": 3.0,
    },
}

resources = {
"t_water": 300.0,
"t_milk": 200.0,
"t_coffee": 100.0,
"t_money": 0.0
}

def check_int(integer):
    while True:
        try:
            value = int(input(integer))
            return value
        except ValueError:
            print("Please insert a digit.")

def calc_coins():
    print(f"Please insert coins.")
    quarters = check_int(f"How many quarters?: ")
    dimes = check_int(f"How many dimes?: ")
    nickles = check_int(f"How many nickles?: ")
    pennies = check_int(f"How many pennies?: ")
    result= (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    return result


def result_coins():
    result = calc_coins()
    if result == MENU[coffee_type]["cost"]:
        print(f"Here is your {coffee_type}☕. Enjoy!")
    elif result > MENU[coffee_type]["cost"]:
        change = result - MENU[coffee_type]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee_type}☕. Enjoy!")
    elif result < MENU[coffee_type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    return result


def check_resources():
    if resources["t_water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry, there is not enough water")
        return False
    elif resources["t_milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk")
        return False
    elif resources["t_coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee")
        return False
    return None


def new_resources():
    result = result_coins()
    if result >= MENU[coffee_type]["cost"]:
        resources["t_water"] -= MENU[coffee_type]["ingredients"]["water"]
        resources["t_milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["t_coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["t_money"] += MENU[coffee_type]["cost"]


to_buy = "start"

while to_buy == "start":
    coffee_type = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    # TODO if espresso
    if coffee_type == "espresso":
        if check_resources() == False:
            break
        new_resources()

    # TODO if latte
    elif coffee_type == "latte":
        if check_resources() == False:
            break
        new_resources()

    # TODO if cappuccino
    elif coffee_type == "cappuccino":
        if check_resources() == False:
            break
        new_resources()

    # TODO if report
    elif coffee_type == "report":
        print(f"Water: {resources['t_water']}ml\n"
              f"Milk: {resources['t_milk']}ml\n"
              f"Coffee: {resources['t_coffee']}g\n"
              f"Money: ${resources['t_money']}")

    # TODO if off
    elif coffee_type == "off":
        to_buy = "off"

    else:
        print(f"Invalid Input. Try again.")