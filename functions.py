import math

def MaxWordLen(listOfWords):
    # Return the longest word of a list of strings
    maxlen = 0
    for word in listOfWords:
        if len(word) > maxlen:
            maxlen = len(word)
    return maxlen


def ReturnRez(w, maxChar, maxlen, nbWord, h, result):
    # Update the character's size if higher
    while maxChar >= 1:
        if ((nbWord * maxChar) <= int(h)) and ((maxChar * maxlen)) <= int(w) and (maxChar >= result):
            result = maxChar
        maxChar -=1

    return result
