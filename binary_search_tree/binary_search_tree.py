import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # base case, tree of 1 value. If value is > insert right, else left
        if value > self.value:

            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target to root, if it's in the root return, else < go left > go right
        # print(self.value, target)
        if self.value == target:
            # print('returning true')
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value > target and self.left:
            return self.left.contains(target)
        else:
            return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        #go right all the way - iterative
        # current = self
        # while current.right:
        #     current = current.right
        # return current.value

        # recursive
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #visit each node one time
        # iterative solution
        stack = Stack()
        stack.push(self)
        while stack.len():
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)

        # recursive solution
        # if self.right:
        #     self.right.for_each(cb)
        # if self.left:
        #     self.left.for_each(cb)
        # return cb(self.value)



        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
               
        # # iterative solution
        # stack = Stack()
        # current = self
        
        # # traverse all the way to the left
        # while current.left:
        #     if current.left:
        #         stack.push(current)
        #     current = current.left
        
        # while stack.len() > 0:
        #     smallest = stack.pop()
        #     if smallest.right:
        #         stack.push(smallest.right)
        #     print(smallest.value)
            
        # recursive solution
        # call fnc on root
        # if left call left
        # if right call right
        # # return print
        # if self.left:
        #     self.in_order_print(self.left)
        # if self.right:
        #     self.in_order_print(self.right)
        # return print(self.value)
        current = self
        if current.left:
            current.left.in_order_print(current.left)
        if current.right:
            current.right.in_order_print(current.right)
        print(current.value)        


        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        queue = Queue()
        queue.enqueue(self)        
        
        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            
            




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make stack
        # call func on root
        # put the root in the stack
        # pop the top item in the stack
        # look right
        # push the right to the stack
        # look left
        # if there is a left push to stack
        # pop the top of the stack

        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            current = stack.pop()
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
