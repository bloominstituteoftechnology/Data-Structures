"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value) 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.pre_order_dft(node)
            node.append(self.value)
        if self.right:
            self.right.pre_order_dft(node)
        return node

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            n = q.dequeue()
            print(n.value)
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.len() > 0:
            n = s.pop()
            print(n.value)
            if n.left:
                s.push(n.left)
            if n.right:
                s.push(n.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        node.append(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)
        return node

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)
        node.append(self.value)
        return node
