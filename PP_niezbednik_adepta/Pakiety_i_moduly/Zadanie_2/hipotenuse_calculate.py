import math

def f_hipotenuse(length1, lenght2):
    result = math.sqrt(math.pow(length1,2)+math.pow(lenght2, 2))
    return result

side1 = float(input("Tell me length of one side of triangle: "))
side2 = float(input("Now tell me length of another side of triangle: "))

hipotenuse = f_hipotenuse(side1, side2)

print("The length of hipotenuse is: ", hipotenuse)