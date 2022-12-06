# the authors names are Cadyn
x = int(input("What is the temperature? \n"))

def temperature(x):
    if x > 78:
        print("Turn on the AC.")
    elif x < 62:
        print("Turn on the heater.")
    else:
        print("It's wonderful weather.")



temperature(x)
