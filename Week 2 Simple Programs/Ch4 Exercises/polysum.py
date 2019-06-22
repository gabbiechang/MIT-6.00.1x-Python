import math

def polysum(n,s):
    area = ((.25*n*s**2)/(math.tan(math.pi/n)))
    perimeterSqrd = (n*s)**2
    return round(area + perimeterSqrd, 4)