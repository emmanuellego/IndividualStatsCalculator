import math
import unittest


class Calculator:

    # Calculator definitions
    def add(a, b):
        return a + b

    def subtr(a, b):
        return a - b

    def multi(a, b):
        return a * b

    def divide(a, b):
        return a / b

    def root(a):
        return math.sqrt(a)

    def nthroot(a, b):
        return b**(a**-1)

    def square(a):
        return a * a

    def power(a, b):
        return math.pow(a, b)

    def addsums(r):
        n = 0
        for i in range(0, len(r)):
            n = Calculator.add(n, r[i])
        return n


if __name__ == "__main__":
    unittest.main()
