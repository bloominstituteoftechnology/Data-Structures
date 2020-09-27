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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if value < self.value:
                # if there is no left child already here
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
            if self.left == None:
                self.left = BSTNode(value)

                # otherwise call insert on the left node
            else:
                self.left.insert(value)

        # otherwise (the new nodes value is greaterthan or equal to the current node value)
        elif value >= self.value:
            # if there is no right child already here
            if not self.right:
            # add the new node to the right
            # create a BSTNode and encapsulate the value in it then set it to the right
                self.right = BSTNode(value)
            else:
            # otherwise call insert on the right node
                self.right.insert(value) 
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

         # if the value of the current node matches the target
         if self.value == target:
             # return True
             return True
        # check if the target is less than the current nodes value
         if self.value > target:
                # if there is no left child already here
            if not self.left:
                return False
                # return False
            else:    
            # otherwise
                return self.left.contains(target)
                # return a call of contains on the left child passing in the target value
                
        # otherwise (the target is greater than the current nodes value)
         else:

            # if there is no right child already here
             if not self.right:
                # return False
                return False
            # otherwise
             else:
                # return a call of contains on the right child passing in the target value
                return self.right.contains(target)

                

    # Return the maximum value found in the tree
    def get_max(self):

        if not self.value:
            return None
        # check for an empty tree
            # return None

        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
        elif not self.right:
            return self.value
            # return the nodes value
        # return a call to get max on the right child
        return self.right.get_max()
        # -----------------------------------------------

        # iterative aproach

        # initialise the max value

        # get a ref to the current node

        # loop while there is still a current node
            # if the current value is greater than the max value, update the max value
            # move on to the next right node

        # return the max value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function passing in the current nodes value
        fn(self.value)

        # if there is a node to the left
        if self.left:
            self.left.for_each(fn)
            # call the function on the left value

        # if there is a node to the right
        if self.right:
            self.right.for_each(fn)
            # call the function on the right node
            


            
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        print(self.value)
        if self.left:
            self.left.in_order_print()
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Create an empty queue
        # add root value to queue
        # while there are items in the queue do the following
        # go to first item in the queue
        # if there is a left value add it
        # if there is a right value add it
        # print the item in the queue that you are on and dequeue it.

        newQueue = []
        newQueue.append(self)
        while len(newQueue):
            current = newQueue.pop(0)
            print(current.value)
            if current.left:
                newQueue.append(current.left)
            if current.right:
                newQueue.append(current.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # Create an empty stack
        # add root value to stack
        # while there are items in the stack do the following
        # go to last item in the stack
        # if there is a left value add it
        # if there is a right value add it
        # print the item in the stack that you are on and dequeue it.

        stack = []
        stack.append(self)
        while len(stack):
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        

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

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
