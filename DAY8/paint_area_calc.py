# Calc how many cans of paint to be ysed for a given wall length and height
import math


def paint_calc(width, height, cover):
    round_calc = math.ceil(((width * height)/cover))
    calc = ((width * height)/cover)
    print(f"For wall of width {width} and height {height}, you need {round_calc}({calc}) can of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
