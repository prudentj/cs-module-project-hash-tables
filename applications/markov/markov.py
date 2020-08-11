import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

wordsArr = words.split()
wordsDict = {}
start
# For all words except the last one

for index in range(len(wordsArr)-1):
    word = wordsArr[index]
    next_word = wordsArr[index+1]

    # If it doesn't exist make a new array in the dictionary with it

    if word not in wordsDict:
        wordsDict[word] = [next_word]
    else:
        wordsDict[word].append(next_word)
    # if the first or second symbols are uppercase make it a start word
    if word.isUpper() or word[1].isUpper():
        if wordDict == {}:
            wordsDict["START"] = [word]
        else:
            wordsDict["START"].append(word)

print(wordsDict)

# TODO: construct 5 random sentences
# Your code here
