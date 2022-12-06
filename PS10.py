# the authors names are: Cadyn Reger
#Write a function that calculate the summation of the odd numbers between any
#two numbers, a and b. Check if the function is working for summation of odd numbers between
#2 and 14 .
def summation_of_odds(a,b):
    total = 0
    for item in range(a+1,b):
        if item % 2 != 0:
            total = total + item


    print(total)


summation_of_odds(2,8)
