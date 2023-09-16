#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

new_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(new_square.area(), new_square.perimeter()))
print(new_square)
