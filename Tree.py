class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            new_left_node = BinaryTree(new_node)
            new_left_node.leftChild = self.leftChild
            self.leftChild = new_left_node

    def insert_right(self, new_node):
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            new_right_node = BinaryTree(new_node)
            new_right_node.rightChild = self.rightChild
            self.rightChild = new_right_node

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild

    def set_root_value(self, new_value):
        self.value = new_value

    def get_root_value(self):
        return self.value


tree = BinaryTree(5)
tree.insert_left(2)
tree.insert_left(4)
tree.insert_right(3)
tree.insert_left(1)
tree.insert_right(6)
print(tree.get_left_child().get_root_value())
print(tree.get_right_child().get_root_value())


def preorder(tree):
    if tree:
        print(tree.get_root_value(),end=' ')
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_value(), end=' ')
        inorder(tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value(), end=' ')


print(preorder(tree))
print(inorder(tree))
print(postorder(tree))
