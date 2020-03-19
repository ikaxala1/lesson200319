import unittest

from src.Fibonacci import fib, memo

def bruteFib(n):
    if n <= 2:
        return 1
    else:
        return bruteFib(n - 1) + bruteFib(n - 2)

class FibonacciTest(unittest.TestCase):
    def testFib1(self):
        self.assertEqual(1, fib(1))
    # def testFib2(self):
    #     self.assertEqual(1, fib(2))
    # def testFib3(self):
    #     self.assertEqual(2, fib(3))
    # def testWithBrute(self):
    #     self.assertEqual(bruteFib(40), fib(40))