#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


"""Define the file name for saving the list"""
filename = "add_item.json"

"""Check if the file exists and load its contents if it does"""
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

"""Add all command line arguments to the list"""
for arg in sys.argv[1:]:
    my_list.append(arg)

"""Save the updated list as a JSON representation"""
save_to_json_file(my_list, filename)

"""Print the updated list"""
print("List after adding arguments:", my_list)
