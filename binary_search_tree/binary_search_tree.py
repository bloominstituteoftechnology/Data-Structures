import sys
print(sys.path)
sys.path.append('queue.py')
sys.path.append('stack.py')
sys.path.append('doubly_linked_list.py')

from queue import Queue
from stack import Stack
from doubly_linked_list import DoublyLinkedList

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
   
Binary search is logrithmic - log(n)
Premature optimization is the root of all evil!
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            #check to see if value is less than parent node
            if value >= self.value:
                #if the right child is not empty, add the value
                if self.right is not None:
                    self.right.insert(value)
                else:
                    #if right child is empty, create the node with the value
                    new_node = BSTNode(value)
                    self.right = new_node
                    
            #check to see if value is greater than parent node        
            if value <= self.value:
                #if the left child is not empty, add the value
                if self.left is not None:
                    self.left.insert(value)
                    
                else:
                    #if left child is empty, create the node with the value
                    new_node = BSTNode(value)
                    self.left = new_node
                    
                    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
            
        else: 
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False            


    # Return the maximum value found in the tree
    #get max goes right
    #if we wanted to get min, we go left
    
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.value
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
            
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------


    #Traversal means you have touched every item once
    #Recursion is much like a call stack
    
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        print(node.value)
        
        if node.right is not None:
            node.in_order_print(node.right)
            
        if node.left is not None:
            node.in_order_print(node.left)
       
       

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #make a queue
        queue = Queue()
        #enqueue the node
        queue.enqueue(node)
        
        while len(queue) > 0: 
            #as long as queue not empty - dequeue what ever is at the front of the queue and make that the current node
            node = queue.dequeue()
            #enqueue the kids of the current node on the queue
            if node.right is not node:
                queue.enqueue(node.right)
                
            if node.left is not node:
                queue.enqueue(node.left)
            print(node.value)                    
        #rinse, wash, repeat
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
         #make a stack
        stack = Stack()
        #push node into stack
        stack.push(node)
        #as long as stack is not empty
        while len(stack) > 0:
            #pop off the stack, this is our current node
            node = stack.pop()
            #put the kids of the current node into the stack
            #check that they are not none before we put onto stack!!
            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)
            print(node.value)
    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
