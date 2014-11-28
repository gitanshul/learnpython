__author__ = 'anshulkhare'
import sys

limit = sys.getrecursionlimit()

def factorial(n):
    """
    :param n: The number whose factorial value needs to be calculated
    :return: The factorial value of n.
    Uses recursion to calculate the factorial
    """
    if n >= limit:
        print("Cannot calculate recursion for a number greater than " + str(limit))
        return False

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

test = 998
print(factorial(test))
