"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
# Key is input value is f(key)
funcDict = {}

# the difference is the key the values will be a list of tuples
difDict = {}

# stores all the sums of all the numbers
sumDict = {}

# This will store the final values
validCombos = []

# Run the function on everything first and store values
for num in q:
    if num not in funcDict:
        funcDict[num] = f(num)

# walk through all combos of sums and differences in q and store them in sumDic and difDict
for numC in q:

    # pulling the numC value from the f(num) dictionary
    funkedNumC = funcDict[numC]

    for numD in q:
        # pulling the numD value from the f(num) dictionary
        funkedNumD = funcDict[numD]

        # computing the difference and sum
        numDif = funkedNumC - funkedNumD
        numSum = funkedNumC + funkedNumD

        # adding that combo to numDif dict with the numDif as the key
        # adds combo to the the list if it doesn't already exist

        # due to the nature of this problem  there is no need to store
        # negative differences if f(x) changes we would need to change this
        if numDif >= 0:
            if numDif not in difDict:
                difDict[numDif] = [(numC, numD)]
            else:
                if (numC, numD) not in difDict[numDif]:
                    difDict[numDif].append((numC, numD))

        # Lets do the same thing for the sum
        if numSum not in sumDict:
            sumDict[numSum] = [(numC, numD)]
        else:
            if(numC, numD) not in sumDict[numSum]:
                sumDict[numSum].append((numC, numD))

# Now we need to see which ones overlap
for key in difDict:
    if key in sumDict:
        # lets now loop through the list in the dict and make tuples out of all combos
        for sumTuple in sumDict[key]:
            for difTuple in difDict[key]:
                newTuple = sumTuple+difTuple
                validCombos.append(newTuple)
# To make it pretty lets sort the tuple list
validCombos.sort()
print(len(validCombos))
# This  f(a) + f(b) = f(c) - f(d) is the same as f(a) + f(b) + f(d)
# We need to walk through all combos of three numbers
# and see if they add up to f(x)
