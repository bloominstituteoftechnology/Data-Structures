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
    def __init__(self, value): # This means that the BSTNode must start with a initial value
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # doing this through recursion
        
        # Will to check if the value is less than or greater than 
        # the current value
        if self.value > value: # Will go left is this is true
            if self.left == None:
                # here we will put the value in 
                self.left = BSTNode(value)
                return
            else:
                # here we are then continuing down the tree
                self.left.insert(value)
        else:
            if self.right == None:
                # This means that we have hit the end
                self.right= BSTNode(value)
                return
            else:
                self.right.insert(value=value)


       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # will do this recursively also
        if self.value == target:
            return True
        # Now working on down the tree
        if self.value > target:  # going down the left part of the tree
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            # going down the right side of the tree
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # using recursion to find the max
        # This means that I will need to traverse the whole tree
        # base case
        val = None

        if self == None:
            return  # might need to change this 

        theMax = self.__our_max(self.left.get_max(), self.right.get_max())

        return max(theMax, self.value)
        

        
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # will go through each of the Nodes in depth form
        if self == None:
            return
        # doing the left side of the tree first
        self.for_each(fn)

        # running the funtion on the value of the node
        fn(self.value)

        # going donw the right side
        self.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # going through the list in recursion
        if self == None:
            return 

        self.left.in_order_print()
        print(self.value)
        self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # making it to implement a queue
        # using the implementation of the queue
        # that we have made to keep track of the nodes we visit
        from data_structures.queue.queue import Queue

        thequeue = Queue()
        # adding everything to the queue
        root = self
        thequeue.enqueue(root)

        #looping through the queue
        while thequeue.size > 0:
            currentNode = thequeue.dequeue()
             # will then add the left and the right children if 
             # they are present
            if currentNode.left != None:
                 # adding to the queue
                 thequeue.enqueue(currentNode.left)
            if currentNode.right != None:
                # adding to the queue
                thequeue.enqueue(currentNode.right)

            print(currentNode.value)
            




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # using a depth first traversal that is iterative
        # importing and using the stack 
        node = self
        while node != None:
            # doing an inner loop that will go into the left side

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

    # This is a function that I created to do the comparison with a none 
    def __our_max(self, val1, val2):
        if val1 == None:
            return val2
        if val2 == None:
            return val1
        else:
            return max(val1, val2)

"""
This code is necessary for testing the `print` methods
"""
#bst = BinarySearchTree(1)
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

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
