class BinaryTree:
    def __init__(self, node):
        self.key = node
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            new_node = BinaryTree(node)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root(self):
        return self.key

    def set_root(self, node):
        self.key = node


root = BinaryTree("A")
root.insert_left(BinaryTree("B"))
root.insert_right(BinaryTree("C"))

b = root.get_left_child()
c = root.get_right_child()

b.insert_right(BinaryTree("D"))

c.insert_left("E")
c.insert_right("F")




