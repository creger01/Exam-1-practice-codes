# the authors names are Cadyn
#Write a function that compare three dierent numbers and returns the minimum.
#Call your function for 206, 405 and 112 .
def maximum_three_numbers(a,b,c):
    if a <= b and a <=c :
        return a
    elif b <= a and b <= c :
        return b
    else:
        return c

maximum_three_numbers(2,25,17)
maximum_three_numbers(25,17,2)
maximum_three_numbers(17,2,25)
