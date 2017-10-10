# Corentin Duhamel

from functions import ReturnRez, MaxWordLen

t = 0
while t < 1 or t > 20:
    print("entrez t")  # Get the number of test cases
    t = input()
    t = int(t)

whsList = []
resultList = []
for i in range(t):
    print('Enter W H S', i+1)  # Get the test cases parameters
    whs = input()

    whsList.append(whs.split(" ", 2))
    words = whsList[i][2].split(" ")  # Put the different entered words in a list

result = 0

for i in range(len(whsList)):  # iterate over the test cases
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





