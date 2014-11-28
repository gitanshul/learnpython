__author__ = 'anshulkhare'

fileName = "words.txt"

fin = open(fileName, 'r')

def moreThan20(f):
    for line in f:
        word = line.strip()
        if len(word) > 20 :
            print(word)

def noE(f):
    counter1 = 0
    counter2 = 0
    for line in f:
        counter1 = counter1 + 1
        word = line.strip().lower()
        if 'e' not in word:
            counter2 = counter2 + 1
            print(word)
    return float(counter2)/float(counter1)


print(noE(fin))

