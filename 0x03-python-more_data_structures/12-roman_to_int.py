#!/usr/bin/python3
def roman_to_int(rom_str):
    if type(rom_str) != str or rom_str is None:
        return 0
    rom_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    result = 0
    for i in range(len(rom_str)):
        if i > 0 and rom_dict[rom_str[i]] > rom_dict[rom_str[i - 1]]:
            result += rom_dict[rom_str[i]] - 2 * rom_dict[rom_str[i - 1]]
        else:
            result += rom_dict[rom_str[i]]
    return result
