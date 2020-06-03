def word_count(s):
    # Your code here
    # ignore=['"',':' ,';',',','.','-','+','=','/',]
    ignore = '":;,.-+=/\\|[]{}()*^&'
    # ignore = '}{":;,.-+=/\|[]()*^&'
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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
