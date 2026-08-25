"""SIMPLE CALCULATOR"""


def add(n1, n2):
    """To add integers"""
    return n1 + n2


def subtract(n1, n2):
    """To subtract integers"""
    return n1 - n2


def multiply(n1, n2):
    """To multiply integers"""
    return n1 * n2


def divide(n1, n2):
    """To divide integers"""
    return n1 / n2


def takes_input():
    num1 = float(input("What's the first number: "))

    for i in operands:
        print(i)

    operand_symbol = input("Pick an operation: ")
    while operand_symbol not in operands:
        Error = "Invalid Input"
        print(Error)
        operand_symbol = input("Pick an operation: ")

    num2 = float(input("What's the second number: "))
    
    operation = operands[operand_symbol]
    first_answer_ = operation(num1, num2)
    print(f"{num1} {operand_symbol} {num2} = {first_answer_}")
    return first_answer_


def cont_inue():
    operand_symbol2 = input("Pick an operation: ")
    while operand_symbol2 not in operands:
        Error = "Invalid Input"
        print(Error)
        operand_symbol2 = input("Pick an operation: ")
        
    num3 = float(input("What's the next number ?: "))

    operation2 = operands[operand_symbol2]
    new_answer_ = operation2(first_answer, num3)


    print(f"{first_answer} {operand_symbol2} {num3} = {new_answer_}")
    
    return new_answer_
    


operands = {
    "+": add,
    "-": subtract,
    "*":  multiply,
    "/": divide
}

print(" Welcome to my SIMPLE CALCULATOR\n _________________________________\n")
first_answer = takes_input()
to_continue = (str(input(f"Type 'c' to continue calculating with {first_answer}, type 'r' to restart or type 'e' to end.: "))).lower()



next_action = True
while next_action is True:
    while to_continue == "c":
        new_answer = cont_inue()
        to_continue = (str(input(f"Type 'c' to continue calculating with {first_answer}, type 'r' to restart or type 'e' to end.: "))).lower() 
        first_answer = new_answer

    while to_continue == "r":
        print(" Welcome to my SIMPLE CALCULATOR\n _________________________________\n")
        first_answer = takes_input()
        to_continue = (str(input(f"Type 'c' to continue calculating with {first_answer}, type 'r' to restart or type 'e' to end.: "))).lower()

    while not to_continue == "c" and not to_continue == "r" and not to_continue == "e":
            print("Invalid Input")
            to_continue = (str(input(f"Type 'c' to continue calculating with {first_answer}, type 'r' to restart or type 'e' to end.: "))).lower()
   
    if to_continue == "e":
        next_action = False

print("GOODBYE")
