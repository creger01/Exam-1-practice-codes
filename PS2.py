# the authors names are Cadyn
#Write a function that takes two parameters for radius and height of a cylinder and
#returns its volume. Check if your function works correctly by passing 10 and 30 as its arguments.
import math
def volume(radius, height):
    area_base = math.pi*radius**2
    volume = area_base * height
    print("The volume is", volume)

volume(10,30)
