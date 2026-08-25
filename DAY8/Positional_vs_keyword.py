# def with 2 Parameters
def greet(name, location):  # name == Parameter
    print(f"Good morning {name}")
    print(f"The weather in {location} is a bit cloudy today")
    print("What would you need help with today?")
    print("OKAY!, Let's get started.")


greet("fareedah", input("Your location"))  # "fareedah", input("Your location") == Positional Arguements
greet(location=input("Your location"), name="Fareedah")
