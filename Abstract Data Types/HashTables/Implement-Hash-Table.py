
# Hash Tables is a data structure that offers a good compromise between speed and memory.
# It is a structure based on an associative array abstract data type that map keys to values.
# An important feature of hash tables is it utilizes a hashing function to store an item associated with a key.
# This allows a quick lookup through its key

# Interview Notes: Make some clarification for some things
# 1) Ask what the key value types are, if they are integers, you do not need to hash
# 2) Talk about collision resolution, for this case we are using chaining with arrays. Linked list is an alternative
# 3) Do we have to worry about load factors?
# 4) Can we assume this all fits in memory?
# 5) Can we assume the inputs are valid?

class HashTable:

    def __init__(self):
        self.cap = 10
        self.table = [None for i in range(self.cap)]

    def set_item(self, key, value):
        curr_key = self.hashing(key)
        new_arr = [key, value]
        if self.table[curr_key] == None:
            self.table[curr_key] = [new_arr]
            return
        for i, k_v in enumerate(self.table[curr_key]):
            if k_v[0] == key:
                self.table[curr_key][i][1] = value
                return
        self.table[curr_key].append(new_arr)

    def get_item(self, key):
        curr_key = self.hashing(key)
        if self.table[curr_key] == None:
            return -1
        for k, v in self.table[curr_key]:
            if k == key:
                return v
        return -1

    def remove_item(self, key):
        curr_key = self.hashing(key)
        if self.table[curr_key] == None:
            return
        for i, k_v in enumerate(self.table[curr_key]):
            if k_v[0] == key:
                del self.table[curr_key][i]
                return

    def hashing(self, key):
        hashed_key = 0
        for char in key:
            hashed_key += ord(char)

        return hashed_key % self.cap


new_table = HashTable()
print(new_table.set_item('strawberries', 10))
print(new_table.set_item('bananas', 5))
print(new_table.get_item('lychee'))
print(new_table.set_item('lychee', 15))
print(new_table.set_item('apples', 1))
print(new_table.get_item('strawberries'))
print(new_table.get_item('bananas'))
