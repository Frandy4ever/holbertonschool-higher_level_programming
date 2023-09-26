#!/usr/bin/python3
"""Defines a function that reads a UTF-8 text file"""

def read_file(filename=""):
  with open(filename, encoding="utf-8") as file:
    print(file.read(), end="")
