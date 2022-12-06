# the authors names are Cadyn
#Write a function that takes time, temp and ratio and calculate and return the
#following formula: maturity = 23.7time^3 + (temp/273) + ln(ratio)
import math
def maturity(time,temp,ratio):
    x = 23.7*(time**3)
    y = (temp/273)
    z = math.log(ratio)
    m = x + y + z
    print(m)

maturity(4,5,6)
