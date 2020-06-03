
cache = {}


def expensive_seq(x, y, z):

    # packaging vars as tuple
    firstkey = (x, y, z)

    def add_to_cache(key):
        # If that key result doesn't exist run the operation
        # and add to cache
        if key not in cache:
            cache[key] = inner_expensive_seq(key)

    def inner_expensive_seq(key):
        if key not in cache:

            # For readability unpack the tuple
            x = key[0]
            y = key[1]
            z = key[2]

            if x <= 0:
                cache[key] = y + z

            if x > 0:
                newkey1 = (x-1, y+1, z)
                newkey2 = (x-2, y+2, z*2)
                newkey3 = (x-3, y+3, z*3)

                add_to_cache(newkey3)
                add_to_cache(newkey2)
                add_to_cache(newkey1)

                result1 = cache[newkey1]
                result2 = cache[newkey2]
                result3 = cache[newkey3]

                cache[key] = result1+result2+result3

        return cache[key]

    return inner_expensive_seq(firstkey)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
