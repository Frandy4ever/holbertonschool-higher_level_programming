#!/usr/bin/python3
# for num in range(100):
#     print(f'{num:02d}', end=', ' if num < 99 else '\n')
# Loop through numbers from 0 to 99.
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
