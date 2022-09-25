from math import *
from fibonacci import *

sequence = []

given_number = int(input("Enter a number: "))
given_number = nearestFibonacci(given_number)
print("The nearest fibonacci number is: " + str(given_number))

for i in range(10):
    given_number = nextFibonacci(given_number)
    sequence.append(given_number)

print("The next 10 fibonacci numbers are: ")
print(sequence)
