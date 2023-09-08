#!/usr/bin/python3
def pow(a, b):
    # Initialize the result to 1.
    result = 1
    
    # Multiply 'a' by itself 'b' times to compute the power.
    for _ in range(b):
        result *= a
    
    # Return the computed result.
    return result