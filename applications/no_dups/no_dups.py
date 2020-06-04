def no_dups(s):
    # Your code here
    wordDict = {}
    words = s.split()
    outputString = ""
    for word in words:
        # If we haven't already added it the dictionary add it to the output
        if word not in wordDict:
            # Adding a space before if it isn't the first word
            if wordDict != {}:
                outputString += " "
            outputString += word
            wordDict[word] = 1
    return outputString


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
