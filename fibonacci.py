from math import *

sequence = []

nearestFibonacci = lambda n, a=0, b=1: a*(2*n<a+b) or nearestFibonacci(n,b,a+b)

def nextFibonacci(n):
    result = ((1 + sqrt(5))/2.0)*n
    return round(result)

given_number = int(input("Enter a number: "))
given_number = nearestFibonacci(given_number)
print("The nearest fibonacci number is: " + str(given_number))

for i in range(10):
    given_number = nextFibonacci(given_number)
    sequence.append(given_number)

print("The next 10 fibonacci numbers are: ")
print(sequence)
