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

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.left is None and self.right is None:
            if target == self.value:
                return True
            else:
                return False

        if target > self.value:
            if self.right.contains(target):
                return True
            else:
                return False
        else:
            if self.left.contains(target):
                return True
            else:
                return False

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            current = self
            value = self.value
            
            while current.right:
                current = current.right
                value = current.value
            
            return value


    def for_each(self, fn):
        # Breadth-first traversal to call function on every node
        current = [self]
        while current:
            next_level = []
            for node in current:
                fn(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level  

    # Part 2 -----------------------

    def in_order_print(self, node):
        # In-Order goes Left > Root > Right
        # Used to sort list by starting with smallest value and working up
        if node is None:
            return

        node.in_order_print(node.left)
        print(node.value)
        node.in_order_print(node.right)

    def bft_print(self, node):
        # Breadth-First Traversal goes through each node level by level
        # Uses a queue and a pointer
        if node is None:
            return

        current = [node]
        while current:
            next_level = []
            for node in current:
                print(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level  

    def dft_print(self, node):
        # Depth-First Traversal is iterative and goes through the left side first followed by the right, starts at designated node
        # Uses a stack and a pointer
        if node is None:
            return
        
        current = [node]
        while current:
            curr_node = current.pop()
            print(curr_node.value)

            if curr_node.right:
                current.append(curr_node.right)
            if curr_node.left:
                current.append(curr_node.left)
        
    # Stretch Goals -------------------------

    def pre_order_dft(self, node):
        # Pre-Order goes Root > Left > Right
        # Used to create a copy of the tree by going from root, down the left, then down the right
        if node is None:
            return
            
        print(node.value)    
        node.pre_order_dft(node.left)
        node.pre_order_dft(node.right)

    def post_order_dft(self, node):
        # Post-Order goes Left > Right > Root
        # Used to delete the tree by removing all child nodes and ending with the root
        if node is None:
            return
            
        node.post_order_dft(node.left)
        node.post_order_dft(node.right)
        print(node.value)