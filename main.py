# Corentin Duhamel
import sys
from functions import ReturnRez, MaxWordLen
from math import *


# Get the text file given as argument
path = sys.argv[1]
text = open(path, 'r')
lines = text.readlines()
text.close()

resultList = []
whsList = []
for i in range(len(lines)):
    if i == 0:
        t = int(lines[i])
    else:
        whsList.append(lines[i].rstrip().split(" ", 2))
result = 0

for i in range(len(whsList)):  # iterate over the test cases
    result = 0
    w = whsList[i][0]
    h = whsList[i][1]
    words = whsList[i][2].split(" ")
    nbWord = len(words)
    maxChar = int(w)
    maxLen = MaxWordLen(words)

    # First, check the score of n words on n lines, n the number of entered words
    result = ReturnRez(w, maxChar, maxLen, nbWord, h, result)

    # Then check scores of group of words
    # Every time two words are grouped, it creates a new word, and remove a line, until we check the score of all the
    # words on the same line.
    for j in range(1, nbWord):
        wordsNew = whsList[i][2].split(" ")
        for k in range(nbWord-j):

            wordsNew[j-1] = wordsNew[j-1] + " " + wordsNew[j]
            del wordsNew[j]
            nbWordNew = len(wordsNew)

            maxLen = MaxWordLen(wordsNew)

            result = ReturnRez(w, maxChar, maxLen, nbWordNew, h, result)

    resultList.append(result)

print(resultList)

for i in range(len(resultList)):
    print("Case #", i, ": ", resultList[i])





