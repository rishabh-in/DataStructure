class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def putItem(self, key, data):

        hashVal = self.hashFunction(key, len(self.slot))

        if self.slot[hashVal] is None:
            self. slot[hashVal] = key
            self. data[hashVal] = data

        else:
            if self. slot[hashVal] == key:
                self. data[hashVal] = data      ## overwrite

            else:
                newHash = self.reHash(hashVal, len(self.slot))
                while self.slot[newHash] is not None and self.slot[newHash] != key:
                    newHash = self.reHash(hashVal, len(self.slot))

                if self. slot[newHash] is None:
                    self.slot[newHash] = key
                    self. data[newHash] = data
                else:
                    self.data[newHash] = data       ## overwrite

    def getItem(self, key):
        start = self.hashFunction(key, len(self.slot))
        stop = False
        found = False
        position = start
        data = None

        while self.slot[position] is not None and not found and not stop:
            if self. slot[position] == key:
                data = self. data[position]
                found = True

            else:
                position = self.reHash(start, len(self.slot))
                if position == start:
                    stop = True
        return data

    def hashFunction(self, key, size):
        return key % size

    def reHash(self, oldHash, size):
        return (oldHash + 1) % size


h = HashTable(5)
h.putItem(1, "Rishabh")
h.putItem(2, "Rishav")

print(h.getItem(2))


