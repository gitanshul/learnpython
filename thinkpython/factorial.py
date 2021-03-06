__author__ = 'anshulkhare'
import sys

limit = sys.getrecursionlimit()


def factorial(n):
    """
    :param n: The number whose factorial value needs to be calculated
    :return: The factorial value of n.
    Uses recursion to calculate the factorial
    """

    if not isinstance(n, int):  # Guardian pattern: Protecting the following code from invalid values.
        print("Not supported for non-integers")
        return
    if n < 0:
        print("Not supported for negative integers")
        return
    if n >= limit:
        print("Cannot calculate recursion for a number greater than " + str(limit))
        return False

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

factorial("a")
