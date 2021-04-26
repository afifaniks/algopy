class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        self.left_child = BinaryTree(node)

    def insert_right(self, node):
        self.right_child = BinaryTree(node)

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


def preorder(root):
    if root == None:
        return

    print(root.key)

    preorder(root.left_child)
    preorder(root.right_child)


def inorder(root):
    if root == None:
        return

    inorder(root.left_child)
    print(root.key)
    inorder(root.right_child)


def postorder(root):
    if root == None:
        return

    postorder(root.left_child)
    postorder(root.right_child)
    print(root.key)


root = BinaryTree("A")
root.insert_left("B")
root.insert_right("C")

b = root.get_left_child()
c = root.get_right_child()

b.insert_right("D")

c.insert_left("E")
c.insert_right("F")

print("Preorder")
preorder(root)
print("Inorder")
inorder(root)
print("Postorder")
postorder(root)