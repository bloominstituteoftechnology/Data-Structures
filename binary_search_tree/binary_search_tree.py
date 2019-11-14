import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.root = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value == None:
        #     self.value = value
        if value < self.value:
            # value less than least, instantiate as child
            if not self.left:
                self.left = BinarySearchTree(value)
            # go to left child and recurse
            else:
                self.left.insert(value)
        if value > self.value:
            # value greater than amx, instantiate as child
            if not self.right:
                self.right = BinarySearchTree(value)
            # go to right child and recurse
            else:
                self.right.insert(value)

        # while value > self.value:
        #     value = self.right
            
        # else:
        #     if value < self.root:
        #         self.left = value
        #     elif value > self.root:
        #         self.right = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # search given key in binary search tree, first compare with
        # root, if key is present at root, return root. if key is greater
        # than root's key, we recur for right subtree of root node.
        # otherwise we recur for left subtree
        if target == self.value:
            return True
        if target > self.value:
            # target larger than max in tree
            if not self.right:
                return False
            # go to right child and recurse
            else:
                return self.right.contains(target)
        if target < self.value:
            # target less than lowest in tree
            if not self.left:
                return False
            # go to left child and recurse
            else:
                return self.left.contains(target)
        
        # return False

        # elif target > self.value:
        #     if target > self.right:
        #         if target < self.value:
        #             if target == self.value:
        #                 return True
        #             else:
        #                 return False
        # elif target < self.value:
        #     if target < self.left:
        #         if target > self.value:
        #             if target == self.value:
        #                 return True
        #             else: 
        #                 return False

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until the end
        # while self.value is not None:
        #     return self.right 

        # if no right child, current max value
        
        # oneliner
        return self.right.get_max() if self.right else self.value

        # recursive 
        # if not self.right:
        #     return self.value
        # # if there is right child, go there and recurse
        # else:
        #     return self.right.get_max()

        #iterative
        # while self.right is not None:
        #     self = self.right

        # return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then go back
        # and go right

        # Oops, don't use 'while'
        # while self.left:
        #     self.left.for_each(cb)
        # while self.right:
        #     self.right.for_each(cb)

        # start at root
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            # print(node.value)
            # self.left.in_order_print(node)
            # self.right.in_order_print(node)

            # print(node.value)
            self.in_order_print(node.left)
            print(node.value)
            # print(node)
            # return node.value
            self.in_order_print(node.right)
            # print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make queue
        queue = Queue()
        current = self
        # push root into queue
        queue.enqueue(current)

        # while queue not empty
        while queue.len() > 0:
            # return current
            current = queue.dequeue()
            # return current
            # print(current)
            # if left add left to back
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            # if right add right to back
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make stack
        stack = Stack()
        current = self

        # call function on root
        stack.push(current)

        while stack.len() > 0:
            current = stack.pop()
            # print(current)   -- needs value
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)





    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
