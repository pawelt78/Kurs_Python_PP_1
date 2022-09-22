import math

def locate_calculation(start_value, percentage, duration):
    finish_value = start_value*math.pow((1+percentage/100),duration)
    return finish_value