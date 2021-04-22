class Node:
    def __init__(self, init_item):
        self.data = init_item
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            current = current.get_next()
            count += 1

        return count

    def search(self, item):
        current = self.head

        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()

        return False

    def remove(self, item):
        current = self.head
        prev = None

        while current != None:
            if current.get_data() == item:
                prev.set_next(current.get_next())
                return
            else:
                prev = current
                current = current.get_next()

    def append(self, item):
        current = self.head
        prev = None

        while current != None:
            prev = current
            current = current.get_next()

        new_node = Node(item)
        prev.set_next(new_node)

    def index(self, item):
        current = self.head
        index = 0

        while current != None:
            if current.get_data() == item:
                return index

            current = current.get_next()
            index += 1

        return -1

    def __str__(self):
        res = "["

        current = self.head
        while current != None:
            res += str(current.get_data()) + ","
            current = current.get_next()

        res += "]"

        return res
