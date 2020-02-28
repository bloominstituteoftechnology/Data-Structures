from dll_queue import Queue
from dll_stack import Stack
import sys
sys.path.append('../queue_and_stack')



class BinarySearchTree:   #rootNode
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  #compare new value with parent node
        if value < self.value: #if value is less than node value check left
              #if something is already there
            if self.left:
                #recurse left
                self.left.insert(value)
                #if not
            else: 
                self.left = BinarySearchTree(value) #assign to class
        #if value >=node.value look right
        if value >= self.value:
        #if something is there already
            if self.right:
                #recurse right
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
            


        

    # Return True if the tree contains the value
    # False if it does not
    
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
            
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
    #if tree is empty return none, if there isnt right return root otherwise return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            return self.left.for_each(cb)
        elif self.right is not None:
            return self.right.for_each(cb)
        else:
            return None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
           self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)
        print(self.value)
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal


#     BFT Steps:
# initialize a queue
# push root to queue
# while stack not empty
# pop top item out of queue into temp
# DO THE THING!!!!!!
# if temp has right right put into queue
# if temp has left left put into queue

    def bft_print(self, node):
        if node is None:
            return
        q = Queue() #make your queue
        q.enqueue(node)#adds to back of queue
        while q.size > 0:
            node = q.dequeue() #remove and return from front of queue
            print(node.value)
            if node.left is not None: #same for left side
                q.enqueue(node.left)
            if node.right is not None: #same for right side
                q.enqueue(node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

#     DFT Steps:
# initialize a stack
# push root to stack
# while stack not empty
# pop top item out of stack into temp
# DO THE THING!!!!!!
# if temp has right right put into stack
# if temp has left left put into stack
    def dft_print(self, node):
        if node is None:
          return
        s = Stack() #make that stack
        s.push(node) #pushhherrrr out 
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
