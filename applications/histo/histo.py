# Your code here
with open("robin.txt") as f:
    words = f.read()


def word_count(s):
    ignore = '":;,.-+=/\\|[]{}()*^&'
    words = s.split()
    counts = {}
    for word in words:
        newWord = ""
        word = word.lower()
        for letter in word:
            whitelisted = True
            for symbol in ignore:
                if symbol == letter:
                    whitelisted = False
                    break
            if whitelisted:
                newWord += letter
        if newWord != '':
            if newWord in counts:
                counts[newWord] += 1
            else:
                counts[newWord] = 1
    return counts


def histogram(s):
    wordCounts = word_count(s)
    # Holder for my tuples
    wordList = []
    # converting the counts to a tuple to be sorted quickly
    for key in wordCounts:
        newTuple = (wordCounts[key], key)
        wordList.append(newTuple)
    wordList.sort(reverse=True)
    # printing the histogram with a legnth of 15 for the words
    for countTuple in wordList:
        output = "#"*countTuple[0]
        print(countTuple[1].ljust(15)[:15] + output)


histogram(words)
