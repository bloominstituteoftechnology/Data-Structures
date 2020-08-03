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

from queue import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #logic: start at root node and loop until 'cur_node' is None
        #if value is <= cur_node insert left, if > cur_node go right
        #need to check if there is already a value, if there isnt add the value
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #need case == value
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if target > self.value:
                if self.right == None:
                    return False
                else: 
                    return self.right.contains(target)
      

    # Return the maximum value found in the tree
    def get_max(self):
        #since > root = right, use right side
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            if node.left:
                #left recursion
                node.in_order_print(node.left)
            print(node.value)
            if node.right:
                #right recursion
                node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #use queue
        #print cur_node
        #add l_child to queue, add r_child to queue, done when queue is empty
        queue = []
        queue.append(self)
        while len(queue) > 0:
            current = queue.pop()
            print(current.value)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #use stack, push some init vals to stack
        #while stack is not empty: pop, print and push
        #done when stack is empty
        stack = []
        stack.append(self)
        while len(stack) > 0:
            #pop root node to traverse the kids on each side
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

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

print("elegant methods")
print("pre order")
#bst.pre_order_dft()
print("in order")
#bst.in_order_dft()
print("post order")
#bst.post_order_dft()  
