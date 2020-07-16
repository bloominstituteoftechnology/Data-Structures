class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, "")

        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, "")

        elif traversal_type == 'levelorder':
            return self.levelorder_print(tree.root)

        elif traversal_type == 'reverse_levelorder':
            return self.reverse_levelorder_print(tree.root)

        else:
            print("""Traversal type " + str(traversal_type) + 
            " is not supported.""")
            return False

    def preorder_print(self, start, traversal):
        """ROOT-->LEFT-->RIGHT"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """LEFT-->ROOT-->RIGHT"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """LEFT-->RIGHT-->ROOT"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        stack = Stack()
        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)

        count = 1

        while stack:
            node = stack.pop()
            if node.left:
                count += 1
                stack.push(node.left)
            if node.right:
                count += 1
                stack.push(node.right)

        return count

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print("-"*50)
print("Pre-Order", tree.print_tree("preorder"))
print("-"*50)
print("In-Order", tree.print_tree("inorder"))
print("-"*50)
print("Post-Order", tree.print_tree("postorder"))
print("-"*50)
print("Level-Order", tree.print_tree('levelorder'))
print("-"*50)
print("Reverse-Level-Order", tree.print_tree("reverse_levelorder"))
print("-"*50)
print("Size of Tree:", tree.size())
print("-"*50)
print("Recursive Size Method:", tree.size_(tree.root))
print("-"*50)
