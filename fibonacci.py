from math import *

nearestFibonacci = lambda n, a=0, b=1: a*(2*n<a+b) or nearestFibonacci(n,b,a+b)

def nextFibonacci(n):
    result = ((1 + sqrt(5))/2.0)*n
    return round(result)
