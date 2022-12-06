#the authors names are Cadyn
import math
def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result


distance(2,4,5,6)
