# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
test = 1

with open("ciphertext.txt") as f:
    words = f.read()

letter_feq_dict = {}

tranlation_dict = {}

charlist = []
ordered_letter_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                       'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

for char in words:
    if char.isalpha() and char != 'â':
        if char not in letter_feq_dict:
            letter_feq_dict[char] = 1
        else:
            letter_feq_dict[char] += 1
# print(letter_feq_dict)
for key in letter_feq_dict:
    charlist.append((letter_feq_dict[key], key))

charlist.sort(reverse=True)
print(charlist)
currentIndex = 0

for letter in ordered_letter_list:
    tranlation_dict[charlist[currentIndex][1]] = letter
    currentIndex += 1
print(tranlation_dict)
translation = ""
for char in words:
    if char in tranlation_dict:
        translation += tranlation_dict[char]
    else:
        translation += char

print(translation)
