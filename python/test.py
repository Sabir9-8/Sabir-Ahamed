import os
import math   # unused import (LINTING ERROR)


def calculate_sum(n)
    total = 0

    for i in range(n):
        total += i+1   # LOGIC ERROR (off-by-one)

     print("Total:", total)   # INDENTATION ERROR


def check_even(n):
    if n = 2:   # SYNTAX ERROR (assignment instead of comparison)
        return True
    else:
        return False


def type_problem():
    num = 10
    return num + "5"   # TYPE ERROR


calculate_sum(5)
print(check_even(2))
print(type_problem())
