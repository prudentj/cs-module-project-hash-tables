# import the linked list structure
from linkedlist import LinkedList

# This is both the node for the linked list and also holds
# the value of the hash table


class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{repr(self.key)}'
        # , {repr(self.value)})


# The lower bound on the number of slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        # rename table to storage
        self.table = [None for _ in range(capacity)]
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return len(self.table)

    def get_load_factor(self):
        # returns the ratio of items to table slots.
        return self.count/len(self.table)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        # obtains the value or memory address in storage that
        # matches that key
        slot = self.table[self.hash_index(key)]
        # Makes a new node to be added to the comment and updates number of objects
        entry = HashTableEntry(key, value)
        self.count += 1
        # If nothing is at that index in the array, pass the memory address of the obj
        if slot is None:
            self.table[self.hash_index(
                key)] = LinkedList(entry)
        # If something is there activate the linked list properties and add it to the end
        else:
            slot.insert(entry)
        # Determines if we need a larger array to update this
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        # if not self.get(key):
        #     print(f'{key} was not found.')
        # else:
        #     self.put(key, None)
        # Your code here
        slot = self.table[self.hash_index(key)]
        if slot and slot.contains(key) is not False:
            self.count -= 1
            slot.remove(key)
        else:
            print("No object exists")
            return False

        if self.get_load_factor() < 0.2:
            self.resize(int(self.capacity/2))

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        slot = self.table[self.hash_index(key)]
        if slot and slot.contains(key) is not False:
            return slot.contains(key)
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY
        self.capacity = new_capacity
        new_table = [None for _ in range(self.capacity)]
        self.count = 0

# Rework this and update comments
        for i in range(len(self.table)):
            if self.table[i] is not None:
                cur = self.table[i].head
                while cur is not None:
                    slot = new_table[self.hash_index(cur.key)]
                    self.count += 1
                    if slot is None:
                        new_table[self.hash_index(cur.key)] = LinkedList(cur)
                        cur = cur.next
                    else:
                        slot.insert(cur)
                        cur = cur.next
        self.table = new_table

        # for current in self.table:
        #     if current is not None:
        #         while current.head is not None:
        # for index in previous hashtable
        # pop off tails until it is empty and run a hashing function and insert into new list
        # delete old list
