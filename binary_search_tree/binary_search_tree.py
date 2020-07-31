from queue import Queue
from stack import Stack

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
        # start at root and loop until 'cur_node' is None
            # if 'value' <= 'cur_node'
                # if 'cur_node.left' is None
                    # insert our value 
                # else 
                    # go left (update 'cur_node' to be 'cur_node.left')
            # elif 'value' > 'cur_node'
                # if 'cur_node.right' is None
                    # insert our value
                # else
                    # go right (update 'cur_node' to be 'cur_node.right')
    
    # recursive approach
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # compare target_value to cur_value
            # 1. == we return True
            # 2. < we go left
            # 3. > we go right
            # 4. if can't go left/right (not found, return False)

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can't go right anymore
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

        #iterative
        # cur_node = self
        # fn(cur_node.value)
        # stack = # nodes you need to backtrack to
        # while cur_node.left:
        #     cur_node = cur_node.left
        #     fn(cur_node.value)
        #     # add node to the stack
        # # pop off the stack
        # # try to go right

    # stretch
    def delete(self, value):
        # different cases
        # if node at bottom level
            # update parent left/right = none
        # if node has only one child
            # parent.left/right = node.left/right
        # if node has two children
            # 'larger' child becomes the parent of its sibling

        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        queue = Queue()

        queue.enqueue(self)
        while queue:
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()

        stack.push(self)
        while stack:
            node = stack.pop()
            print(node.value)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
