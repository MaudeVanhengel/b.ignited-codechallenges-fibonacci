from ast import main
import unittest
from fibonacci import *

class TestFibonacci(unittest.TestCase):

    def test_nearestFibonacci(self):
        self.assertEqual(nearestFibonacci(4), 5)
        self.assertEqual(nearestFibonacci(30), 34)
        self.assertEqual(nearestFibonacci(3), 3)
        self.assertEqual(nearestFibonacci(830000), 832040)
        self.assertEqual(nearestFibonacci(-3), 1)
        
    def test_nextFibonacci(self):
        self.assertEqual(nextFibonacci(1), 2)
        self.assertEqual(nextFibonacci(89), 144)
        self.assertEqual(nextFibonacci(514229), 832040)
        self.assertEqual(nextFibonacci(1134903170), 1836311903)

if __name__ == '__main__':
    unittest.main()