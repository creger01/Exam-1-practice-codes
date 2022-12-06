# the authors names are Cadyn
#Write a function that compares three dierent numbers and returns the maximum.
#Call your function for 2, 25, and 17 .
def maximum_three_numbers(a,b,c):
    if a >= b and a >=c :
        return a
    elif b >= a and b >= c :
        return b
    else:
        return c
