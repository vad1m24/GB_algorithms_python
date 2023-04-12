class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List1:
    def __init__(self, data):
        new_node = Node(data)
        self.start_node = new_node

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
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node

    def delete_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next


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


l1 = List1(4)
l1.insert_start(3)
l1.insert_start(2)
l1.insert_end(5)
l1.print_l()
l1.delete_start()
l1.delete_end()
l1.print_l()
print(l1.search(4))
print(l1.search(10))


