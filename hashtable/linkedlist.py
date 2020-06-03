class LinkedList:
    def __init__(self, HashTableEntry=None):
        self.head = HashTableEntry
        self.tail = HashTableEntry

    def __repr__(self):
        return f'{repr(self.head)}'

    # Inserts a node at the tail of the linked list
    def insert(self, HashTableEntry):
        new_entry = HashTableEntry
        if self.head is None:
            self.head = new_entry
            self.tail = new_entry
        elif self.contains(HashTableEntry.key) is not False:
            current = self.head
            while current is not None:
                if current.key == HashTableEntry.key:
                    current.value = HashTableEntry.value
                    break
                else:
                    current = current.next
        else:
            self.tail.next = new_entry
            self.tail = new_entry

    def contains(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return False

    def remove(self, key):
        if self.head.key == key:
            deadNode = self.head
            self.head = self.head.next
            deadNode.next = None
        else:
            current = self.head
            prev = None
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    current.next = None
                    return current.value
                prev = current
                current = current.next
            return False
