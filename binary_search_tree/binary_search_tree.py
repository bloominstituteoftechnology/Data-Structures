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
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right == None:
             self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target==self.value:
            print('this should return True')
            return True
        if target < self.value:
            # print('this is the value when its bigger than target',self.value)
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            # print('this is the value when its smaller than target',self.value)
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right==None:
            return self.value
        else:
            return self.right.get_max()
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if not self.right==None:
            self.right.for_each(cb)
        if not self.left==None:
            self.left.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return 
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

            
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()                 
        queue.enqueue(node)             
        while queue.len() > 0:                
            popped = queue.dequeue()                              
            print(popped.value)   
            if popped.left:                          
                queue.enqueue(popped.left)
            if popped.right:                                       
                queue.enqueue(popped.right)
            

        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()                                           
        stack.push(node)                              
        while stack.len() > 0:                               
            popped = stack.pop()                              
            print(popped.value)                  
            if popped.left:                                       
                stack.push(popped.left)
            if popped.right:                                        
                stack.push(popped.right)
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
bt = BinarySearchTree(5)
bt.insert(2)
bt.insert(3)
bt.insert(7)
bt.insert(30)
bt.insert(10)
# print(bt.left.right.value)
bt.in_order_print(bt)
