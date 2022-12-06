# the authors names are Cadyn
#Dene two functions: one that returns the area of a circle and the other that returns
#the area of a square. Ask yourself what should be the parameter for each of these functions?
#Now, use these functions and dene a third function that takes the radius of the circle and
#length of the square and return the area enclosed between a circle inside a square.
import math
def area_circle(radius):
    area_c = math.pi*radius**2
    return area_c
#print("The area of the circle is", area_c) CANNOT PRINT IF I AM GOING TO CALL THIS FUNCTION LATER ON

def area_square(length):
    area_s = length ** 2
    return area_s
    #print("The area of the square is", area_s) CANNOT PRINT IF I AM GOING TO CALL THIS FUNCTION LATER ON

def area_enclosed(radius, length):
    area_e = area_square(length) - area_circle(radius)
    return area_enclosed


area_enclosed(6, 10)
