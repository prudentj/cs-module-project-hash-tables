
# This solution is O(2^n) time complexity
# def fib(n):
#     if n <=1
#         return n
#     return fib(n-1) + fib(n-2)

# Memoization, top-down dynamic programing
cache = {}
# This has O(n)^2 or O(n) not sure time complexity and at the expense of time
# Note python has a recursion limit of 98


def fib(n):
    if n <= 1:
        return n
    # if n is not a key in the cache add it to the cache
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


for i in range(95):
    print(f"{i:3} {fib(i)}")


# Example of argument of really expensive funciton
# great if you are making a lot of the same function calls it will help
# if every unique call it has to put it in cache

# def expense_function(x,y):
#     key=(x,y)

#     if key not in cache:
#         cache[key] = whatever expression you want
#     return cache [key]


# print(d.values())
# items = list(d.items())

# # sort by acending key
# items.sort()
# print(items)

# # sort descending by key
# items.sort(reverse=True)

# print(items)

# sort ascending by value
"""
def get_key(e): # e is going to be the tuple
    # Return the thing that we want to sort by
    return e[1]

items.sort(key=get_key)
"""
# items.sort(key)


# find the counts of letters with n complexity time
def print_letter_count(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    print(counts)


print_letter_count("aaaaabbbbcbccca")

# Caesar Cipher
​
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}
​
decode_table = {}
​


def build_decode_table():
    for key, value in encode_table.items():
        decode_table[value] = key


​


def encode(s):
    r = ""


​
  for c in s:
       if c in encode_table:
            r += encode_table[c]
        else:
            r += c
​
  return r
​
​


def decode(s):
    r = ""


​
  for c in s:
       if c in decode_table:
            r += decode_table[c]
        else:
            r += c
​
  return r
​
build_decode_table()
​
print(encode("HELLO, WORLD!"))
​
print(decode("DOGGE, BEUGW!"))
​
