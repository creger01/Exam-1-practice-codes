# the authors names are Cadyn
#Write a function that takes the height (unit: inch) and weight (unit: lb) and cal-
#culates the body mass index (BMI).
def bmi_calc(x,y):
    height = x * 0.0254
    weight = y * 0.45369237
    BMI = weight / height**2
    print("Your BMI is", BMI)


bmi_calc(62,117)
