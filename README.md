# b.ignited codechallenge: fibonacci

### Prerequisites

- Python 3

### Run

`python3 main.py`

### Test

`python3 -m unittest test_fibonacci.py -v`

### Description:

De bedoeling is om de 10 volgende getallen van de fibonnaci reeks te berekenen op basis van een input getal. Bv. Input: 3 Output: 5,8,13,21,34. Hou er echter rekening mee dat dit input getal ook geen lid kan zijn van de fibonnaci reeks. In dit geval neem je de dichtsbijzijnde optie. En als laatste, hou zeker in het achterhoofd dat het input getal ook in de duizende kan zitten.

### Solution:

1. Created a lambda "nearestFibonacci". Based on [this](https://codegolf.stackexchange.com/a/133437) codegolf code. [Why invent the wheel again ;-)]

> Iterates through pairs of consecutive Fibonacci numbers (a,b) until it reaches one where the input n is less than their midpoint (a+b)/2, then returns a.

2. Created a function "nextFibonacci" which calculates the next fibonacci number from a given_number.
This is repeated 10 times to calculate the sequence of 10 numbers.


