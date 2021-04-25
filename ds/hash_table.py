class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key, size):
        return key%size

    def rehash(self, old_hash, size):
        return (old_hash + 1)%size

    def put(self, key, data):
        hash_value = self.hash(key, self.size)

        if self.slots[hash_value] == None or \
                self.slots[hash_value] == key:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            next_slot = self.rehash(hash_value, self.size)
            while self.slots[next_slot] != None:
                next_slot = self.rehash(next_slot, self.size)
            if self.slots[next_slot] == None or \
                    self.slots[hash_value] == key:
                self.slots[next_slot] = key
                self.data[next_slot] = data

    def print(self):
        print("=======================================")
        for i in range(self.size):
            print(self.slots[i], "->", self.data[i])
        print("=======================================")

    def get(self, key):
        start_slot = self.hash(key, self.size)
        current = start_slot

        # Return None if nothing inserted
        if self.slots[current] == None:
            return None

        if self.slots[current] == key:
            return self.data[current]

        current = self.rehash(current, self.size)

        while self.slots[current] != key and current != start_slot:
            current = self.rehash(current, self.size)

        if self.slots[current] == key:
            return self.data[current]

        return None

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


data = 32
map = HashTable()
map.put(1, "Anik")
map.put(9, 13)
map.put(10, "Narcissist")
map.put(11, "Anik")
map.put(312, "Myself")
map.print()
map[21] = "Onik"
map.print()

print(map[21])
print(map[312])



