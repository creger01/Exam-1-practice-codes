# the authors names are: Cadyn
def total_count_odds(a,b):
    total = 0
    for item in range(a+1,b):
        if item % 2 != 0:
            total = total + 1


    print(total)


total_count_odds(2,5)
