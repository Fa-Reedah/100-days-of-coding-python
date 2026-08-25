import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

colors_list = [(42, 94, 150), (182, 43, 75), (227, 207, 99), (209, 155, 88), (180, 169, 30), (140, 88, 59),
               (118, 176, 208), (202, 73, 122), (214, 129, 173), (231, 68, 47), (92, 102, 189), (143, 32, 60),
               (46, 165, 116), (50, 55, 96), (19, 154, 84), (116, 45, 35), (122, 217, 209), (33, 183, 194),
               (226, 170, 188), (121, 192, 172), (43, 49, 67), (215, 205, 34), (84, 39, 29), (175, 186, 219),
               (230, 173, 164), (156, 207, 218), (38, 78, 83), (86, 29, 52), (24, 95, 94), (33, 62, 61), (84, 73, 40)]


tim = Turtle()
tim.speed(0)
tim.penup()
start_x = -270
start_y = -200

tim.goto(start_x, start_y)


def horizontal():
    for i in range(9):
        tim.dot(15, random.choice(colors_list))
        tim.forward(50)
        tim.penup()
        tim.dot(15 , random.choice(colors_list))


def nxt_line():
    global start_y
    current_y = start_y + 50
    tim.penup()
    tim.goto(start_x, current_y)
    start_y = current_y


for k in range(10):
    horizontal()
    nxt_line()

tim.hideturtle()

screen = Screen()
screen.exitonclick()

# rgb = []
#
# colors = colorgram.extract('Hirst_spot.jpg', 60)
# for i in colors:
#     color_num = (i.rgb.r, i.rgb.g, i.rgb.b)
#     #print(color_num)
#     rgb.append(color_num)
#
# print(colors)
# tim = Turtle()