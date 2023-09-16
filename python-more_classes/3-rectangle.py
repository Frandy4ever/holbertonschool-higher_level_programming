#!/usr/bin/python3


Rectangle = __import__('3-rectangle').Rectangle

new_gect = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(new_gect.area(), new_gect.perimeter()))

print(str(new_gect))
print(repr(new_gect))

print("--")

new_gect.width = 10
new_gect.height = 3
print(new_gect)
print(repr(new_gect))
