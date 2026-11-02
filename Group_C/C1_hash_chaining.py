# Experiment C1: Hash Table with Chaining
# Group C: Hashing

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        print(f"Inserted ({key}: '{value}') at index {index}")

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key} from index {index}")
                return True
        print(f"Key {key} not found for deletion")
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
    ht = HashTableChaining(10)
    ht.insert(12, "Apple")
    ht.insert(22, "Banana")  # Collision at index 2
    ht.insert(35, "Cherry")
    ht.display()

    print(f"Search key 22: {ht.search(22)}")
    ht.delete(12)
    ht.display()
