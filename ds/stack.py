class Stack:
    """
    Stack implementation.
    Supported methods:
    1. Push
    2. Pop
    3. Peek
    4. isEmpty
    5. size
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []






