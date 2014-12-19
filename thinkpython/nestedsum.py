__author__ = 'anshulkhare'


def nested_sum(t):
    sum = 0
    for item in t:
        if isinstance(item, list):
            sum += nested_sum(item)
        else:
            sum += item
    return sum

t = [[4,5,6],[7,8,[10, 10, 10]],1,2,3]

print(nested_sum(t))

