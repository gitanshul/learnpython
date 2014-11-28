__author__ = 'anshulkhare'


def reverse(mystr):
    return mystr[::-1]


def isPalindrome(mystr):
    return mystr == reverse(mystr)

test = "anshul"
test2 = "nitin"

print(isPalindrome(test))
print(isPalindrome(test2))