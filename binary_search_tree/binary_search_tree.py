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
            if self.left:
                #recurse left
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                #recurse right
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)    
    #planning it out:
    # base case is:
    #check if empty put node  here at root
        
    # else compare if new is less than node.value
    # leftnode.insert,value    
    # go left
      
            
    # and if its bigger, go right
    # rightnode.insert.value
    # every node is binary search tree

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == None:
            return False
        if target == self.value:
            return True
    
    # so compare
    # if node is none return false 
    # or
    # if node.value == find_value
    # return true
    
    
    # else
    # if find_value < node.value
    # if node.left
    # find_value on left node
    # same for right 
    # else
    # if node.right
    # find on right node
        elif self.value > target:
            if self.left:
                return self.left.contains(target) 
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
        return False
    

    # Return the maximum value found in the tree
    def get_max(self):
        
    
    # to get max follow the right to the end
        if self.right == None:
            return self.value
        
    # if there is a right
    # get max on right
    #els
        else:
            return self.right.get_max()
    # return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)


        if self.right != None:
            self.right.for_each(cb)

#  executing the passed-in callback function on each tree node value. 
#  There is a myriad of ways to perform tree traversal;
#    in this case any of them should work. 


    
    
    

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if anything on left print left
        if node.left is not None:
            node.left.in_order_print(node.left)
        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        # as long as the node is not empty keep pushing to que qith temp val
        while queue.size > 0:
            temp_val = queue.dequeue()
            print(temp_val.value)
            if temp_val.right is not None:
                queue.enqueue(temp_val.right)
            if temp_val.left is not None:
                queue.enqueue(temp_val.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        my_stack = Stack()
        my_stack.push(node)
        while my_stack.len() > 0:
            temp = my_stack.pop()
            print(temp.value)
            if temp.left is not None:
                my_stack.push(temp.left)
            if temp.right is not None:
                my_stack.push(temp.right)
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
