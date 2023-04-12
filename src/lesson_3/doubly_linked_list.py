class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List2:
    def __init__(self):
        self.start_node = None

    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def delete_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_end(self):
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None

    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False


l2 = List2()
l2.insert_start(3)
l2.insert_start(2)
l2.insert_end(4)
l2.insert_end(1)
l2.insert_end(5)
l2.print_l()
#l2.delete_start()
#l2.delete_end()
#l2.print_l()
print(l2.search(3))
print(l2.search(10))
