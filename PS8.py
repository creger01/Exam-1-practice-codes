# the authors names are Cadyn
#Write a function that takes two numbers and find the summation of all the numbers
#between these two numbers. Check how your function is working by passing 1 and 5 to it.
#What will you get if you pass 20 and 113 to your function?
def summation(x,y):
    total = 0
    for item in range(x+1,y):
            total = total + item
    print(total)


summation(1,5)
summation(20,113)
