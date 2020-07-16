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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):

        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()




class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
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
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return  False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        current = self

        # loop down to find the rightmost leaf
        while (current.right):
            current = current.right
        return current.value


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
    def in_order_print(self, node=None):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)

        if self.right is not None:
            self.right.in_order_print()
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        # you should import the queue class from earlier in the week
        # and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"
        queue = Queue()
        # start by placing the root in the queue
        queue.enqueue(self)
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while len(queue) > 0:
            # dequeue item from front of queue
            # print that item
            current = queue.dequeue()
            print(current.value)
            # place current item's left node in queue if not None
            if current.left is not None:
                queue.enqueue(current.left)
                # place current item's right node in queue if not None
            if current.right is not None:
                queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        # initialize an empty stack
        empty_stack = Stack()
        # push the root node onto the stack
        empty_stack.push(self)
        # need a while loop to manager our iteration
        while len(empty_stack) > 0:

        # if stack is not empty enter the while loop

            # pop top item off the stack
            item = empty_stack.pop()
            # print that item's value
            print(item.value)


            # if there is a right subtree
            if item.right is not None:
                empty_stack.push(item.right)
                # push right item onto the stack
            if item.left is not None:
                empty_stack.push(item.left)
            # if there is a left subtree
                # push left item onto the stack



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)

            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)


            print(node.value)




bnt = BSTNode(20)
bnt.insert(3)
bnt.insert(3232)
bnt.insert(4232)
arr = []
cb = lambda x: arr.append(x * 5)
bnt.for_each(cb)
print(arr)

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)


