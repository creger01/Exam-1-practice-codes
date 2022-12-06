# the authors names are: Cadyn
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        old = factorial(n-1)
        result = n * old
        return result


factorial(8)
#40320
