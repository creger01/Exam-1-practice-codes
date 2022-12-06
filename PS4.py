# the authors names are Cadyn
#Write a function that checks if a number is divisible by 5 or not. If it was, returns
#"Yes, it is!" , and if it wasn't, return "No, it is not!"
import math
def is_divisible (x):
    if x % 5 == 0:
        return "Yes, it is!"
    else:
        return "No, it is not"


is_divisible(10)
is_divisible(25)
is_divisible(27)
