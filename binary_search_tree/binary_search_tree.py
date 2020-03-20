import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, value):
        result = ''

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return
        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left is not None:
            self.left.for_each(cb)

        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Inorder (l,root, r):
    # Preorder
    # Postorder

    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(self.value)

        if node.right is not None:
            node.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
         pass
        # create a queue for nodes
        # add current node to queue
        # whitle the queue isn't empty
            # dequeue a node from the queue
            # print the node value
            # add its children to the queue
                    # i.e add left child
                    # add right (if you can)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # create a node stack
        # push the current node onto stacks
        # whilte we have itmes on stack
            #print the current value and pop it off
            #push  the right value of the current node if we can find it
            #push the left value of the current node if we can

        # stack = []
        # # pus the left node
        # while len(stack) > 0:
        #     if node.left is not None:
        #         stack.append(node.left)
        #
        #     stack.append(self)
        #
        #     if node.right is not None:
        #         stack.append(node.right)
        #
        #     popped = stack.pop()
        #     print(popped)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(4)
bst.insert(2)




