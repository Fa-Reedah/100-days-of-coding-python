#from another_module import var
#tom = var
#print(tom)

# from turtle import Turtle, Screen     # from module, import class
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("darkgreen")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()           # object = class
# print(my_screen.canvheight)    # object.attribute(it has)
# my_screen.exitonclick()         # object.method()(can do)

from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)