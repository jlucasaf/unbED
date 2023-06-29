class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

    def __str__(self):
        if self.left == self.right == None:
            left = right = ''
        else:
            left = str(self.left) if self.left else '()'
            right = str(self.right) if self.right else '()'
        return f'({self.data}{left}{right})'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root) if self.root else ''

    def __contains__(self, data):
        def contains(root, data):
            if root is None:
                return False
            if root.data == data:
                return True
            if root.data < data:
                return contains(root.right, data)
            return contains(root.left, data)

        return contains(self.root, data)

    def add(self, data):
        def insert(root, data):
            if root is None:
                return Node(data)
            if root.data < data:
                root.right = insert(root.right, data)
            else:
                root.left = insert(root.left, data)
            return root

        self.root = insert(self.root, data)

    def inorder(self, process=lambda x: print(x.data, end=' ')):
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                process(root)
                inorder_traversal(root.right)

        inorder_traversal(self.root)

    def postorder(self, process=lambda x: print(x.data, end=' ')):
        def postorder_traversal(root):
            if root:
                postorder_traversal(root.left)
                postorder_traversal(root.right)
                process(root)

        postorder_traversal(self.root)

    def preorder(self, process=lambda x: print(x.data, end=' ')):
        def preorder_traversal(root):
            if root:
                process(root)
                preorder_traversal(root.left)
                preorder_traversal(root.right)

        preorder_traversal(self.root)
