def start():
    lst = List()
    lst.insert_start(2)
    lst.insert_start(3)
    lst.insert_end(4)
    lst.insert_end(1)
    lst.insert_end(5)
    lst.print_l()
    lst.revers()  # 1. Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
    lst.print_l()
    lst.sort()  # 2. Реализовать сортировку пузырьком для двухсвязного списка
    lst.print_l()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
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

    def revers(self):  # <- Метод разворота связного списка
        n = self.start_node
        previous = None
        if self.start_node is None:
            print("список пустой")
            return
        while n.next:
            tmp = n.next
            n.next = previous
            previous = n
            n = tmp
        n.next = previous
        self.start_node = n

    def sort(self):  # <- Сортировка пузырьком для двухсвязного списка
        n = self.start_node
        if self.start_node is None:
            print("список пустой")
            return
        while n.next:
            i = n.next
            while i:
                if n.data > i.data:
                    tmp = i.data
                    i.data = n.data
                    n.data = tmp
                i = i.next
            n = n.next
