# Experiment C2: Hash Table with Linear Probing
# Group C: Hashing

class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        start = self._hash(key)
        for i in range(self.size):
            idx = (start + i) % self.size
            if self.table[idx] in (None, self.DELETED, key):
                self.table[idx] = key
                print(f"Inserted key {key} at index {idx}")
                return True
        print("Hash Table is full!")
        return False

    def search(self, key):
        start = self._hash(key)
        for i in range(self.size):
            idx = (start + i) % self.size
            if self.table[idx] is None:
                return -1
            if self.table[idx] == key:
                return idx
        return -1

    def delete(self, key):
        idx = self.search(key)
        if idx != -1:
            self.table[idx] = self.DELETED
            print(f"Deleted key {key} from index {idx}")
            return True
        print(f"Key {key} not found")
        return False

    def display(self):
        print("Hash Table:", [f"{i}:{val}" for i, val in enumerate(self.table) if val is not None])


if __name__ == "__main__":
    ht = HashTableLinearProbing(10)
    ht.insert(14)
    ht.insert(24)  # Collides with 14 -> probes to index 5
    ht.insert(34)  # Collides with 14, 24 -> probes to index 6
    ht.display()

    print(f"Key 34 found at index: {ht.search(34)}")
    ht.delete(24)
    ht.display()
    print(f"Key 34 found after deleting 24 at index: {ht.search(34)}")
