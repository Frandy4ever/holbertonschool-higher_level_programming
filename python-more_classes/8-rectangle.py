#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

new_rectangle_1 = Rectangle(8, 4)
new_rectangle_2 = Rectangle(2, 3)

if new_rectangle_1 is Rectangle.bigger_or_equal(new_rectangle_1, new_rectangle_2):
    print("new_rectangle_1 is bigger or equal to new_rectangle_2")
else:
    print("new_rectangle_2 is bigger than new_rectangle_1")


new_rectangle_2.width = 10
new_rectangle_2.height = 5
if new_rectangle_1 is Rectangle.bigger_or_equal(new_rectangle_1, new_rectangle_2):
    print("new_rectangle_1 is bigger or equal to new_rectangle_2")
else:
    print("new_rectangle_2 is bigger than new_rectangle_1")
