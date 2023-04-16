class Hash_table:
    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]

    def hash(self, key):
        return key % self.size


    def insert(self, key, val):  # key = 10 val = 'dsds'
        index = self.hash(key)   # index = 0
        for i in range(len(self.table[index])):  # [[0, 'fdg'], [10,'gffg'], [100,'fggffg']]
            if self.table[index][i][0] == key:
                self.table[index][i][1] = val
                return
        self.table[index].append([key, val])

    def print_hash(self):
        for i in self.table:
            if len(i) != 0:
                print(*i)
        print()

    def search(self, key):
        index = self.hash(key)
        for i in self.table[index]:
            if key == i[0]:
                return i[1]
        return None

hash_tab = Hash_table()
hash_tab.insert(10, 'q')
hash_tab.insert(100, 'w')
hash_tab.insert(11, 'a')
hash_tab.insert(12, 'z')
hash_tab.insert(112, 'p')
hash_tab.print_hash()
hash_tab.insert(112, 'q')
hash_tab.print_hash()
print(hash_tab.search(11))
print(hash_tab.search(13))
