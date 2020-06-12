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
from queue import QueueFromArray as Queue
from stack import LinkedListStack as Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # checks for value on left
            if not self.left:
                self.left = BSTNode(value)
            # Inserts on left
            else:
                self.left.insert(value)
        else:
            # checks for right node and sets it
            if not self.right:
                self.right = BSTNode(value)
            else:
                # inserts on the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                #checks if contains again
                return self.left.contains(target)
        else:
            if self.right:
                #checks if contains again
                return self.right.contains(target)
        #is not contained
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        # will rewrite current node right
        while current_node.right:
            current_node = current_node.right
        return current_node.value

        # if self.right is None:
        #     return self.value
        # else:
        #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #keeps checking left until no more
        if self.left:
            self.left.in_order_print(node)
        #if no left then prints
        print(self.value)
        #goes to right side
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # hold all nodes in order
        queue = Queue()

        # add current node
        queue.enqueue(node)

        #loop so long as queue still has elements
        while len(queue) > 0:
            #takes current off queue and prints value
            current = queue.dequeue()
            print(current.value)

            if current.left:
                #adds node to left to queue
                queue.enqueue(current.left)
            
            if current.right:
                #adds node to right to queue
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # hold all nodes in the order they were accessed
        stack = Stack()

        # add current node
        stack.push(node)

        #loop so long as stack still has elements
        while len(stack) > 0:

            current = stack.pop()
            print(current.value)

            # go in ascending order by pushing the right branch first
            if current.right:
                stack.push(current.right)
              
            if current.left:
                stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
