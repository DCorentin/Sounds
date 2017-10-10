def MaxWordLen(listOfWords):
    # Return the longest word of a list of strings
    maxlen = 0
    for word in listOfWords:
        if len(word) > maxlen:
            maxlen = len(word)
    return maxlen


def ReturnRez(w, maxChar, maxlen, nbWord, h, result):
    # Update the character's size if higher
        while int((int(w) / maxChar)) < maxlen:
            maxChar -= 1

        if ((nbWord * maxChar) <= int(h)) and (maxChar >= result):
            result = maxChar
        return result
