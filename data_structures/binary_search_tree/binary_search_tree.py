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


    # created an inner function so that I can pass in the node 
    # into each of the functions
    def get_max_recurs(self, node):
        if node == None:
            return
        
        val = node.__our_max(node.get_max_recurs(node.left), node.get_max_recurs(node.right))
        return node.__our_max(val, node.value)
        
    # Return the maximum value found in the tree
    def get_max(self):
        # using recursion to find the max
        # This means that I will need to traverse the whole tree
        # base case
        if self.value == None:
            return None
        #putting in the node
        node = self
        val = self.get_max_recurs(node)
        return val
        

        
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # will go through each of the Nodes in depth form
        if self == None:
            return
        # doing the left side of the tree first
        if self.left != None:
            self.left.for_each(fn)

        # running the funtion on the value of the node
        fn(self.value)

        # going down the right side
        if self.right != None:
            self.right.for_each(fn)

    # Part 2 -----------------------


    def in_order_print_recur(self, node):
        """
        This is the recursion function that will 
        print in the order
        """
        if node == None:
            return
        
        node.in_order_print_recur(node.left)
        print(node.value)
        node.in_order_print_recur(node.right)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # making the in_order_print a wrapper that will 
    # be able to either use the self as the 
    # starting node or will use the node that
    # is passed into the in_order_print funtion.
    # calls the function in_order_print_recur(node)
    def in_order_print(self, node=None):
        # setting up to call the recursive function
        if node == None:
            node = self
        # calling the recurs print function
        self.in_order_print_recur(node)

        

    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, theNode=None):
        # making it to implement a queue
        # using the implementation of the queue
        # that we have made to keep track of the nodes we visit
        from data_structures.queue.queue import Queue

        thequeue = Queue()
        # adding everything to the queue
        # checking to either use the self as the root or 
        # the passed in node
        if theNode == None:
            theNode = self

        root = theNode
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
    def dft_print(self, node=None):
        # using a depth first traversal that is iterative
        # importing and using the stack that we have created
        visited = []
        from data_structures.stack.stack import Stack
        # checking to see where we will get the first node
        if node == None:
            node = self
        #putting on to the stack the root node
        my_stack = Stack()
        my_stack.push(node)
        # will then mark the node as visited
        visited.append(node)
        while my_stack.size > 0:
            # will first pop the top node off the stack
            currNode = my_stack.pop()
            # will then add its children (neighbors if they are not in the visited list)
            # on to the stack
            if currNode.right is not None and currNode.right  not in visited:
                my_stack.push(currNode.right)
                visited.append(currNode.right)
            # doing the same thing for the left side
            if currNode.left is not None and currNode.left not in visited:
                my_stack.push(currNode.left)
                visited.append(currNode.left)
            # will now do the printing of the value of the current node
            print(currNode.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # making the inner pre_order_recus
    # function
    def pre_order_recurs(self, node):
        # base case
        if node == None:
            return
        print(node.value)

        self.pre_order_recurs(node.left)
        self.pre_order_recurs(node.right)

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node=None):
        # Tyring my preorder traversal of the binary tree
        # visiting the root node and then will 
        # go and viist the left subtree
        # and then visit the right subtree
        # checking to see if the node that is passed in is null or not
        if node == None:
            node = self
        self.pre_order_recurs(node)


    # This the inner funtion that is recursive and is called
    # from the post_order_dft function
    def post_order_dft_recurs(self, node):
        # base case 
        if node == None:
            return
        self.post_order_dft_recurs(node.left)
        self.post_order_dft_recurs(node.right)

        # Will now pring the node
        print(node.value)
    # Print Post-order recursive DFT
    # making this be a wrapper the the recursive function
    def post_order_dft(self, node=None):
        if node == None:
            node = self
        self.post_order_dft_recurs(node)
        

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
bst.in_order_print()
print("post order")
bst.post_order_dft()  
