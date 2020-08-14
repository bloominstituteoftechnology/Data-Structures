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

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # first check if the input value is less than the root.
        if value < self.value:
            # if it is less than the root, check if there is a child
            # to the left
            if self.left:
                # if there is a child to the left, call the insert function
                # on that child
                self.left.insert(value)
            #if the above is false, create the child to the left
            else:
                # assign the left of the root to be the new input node inserted
                self.left = BSTNode(value)
        # if the input fails the first if statement, it automatically
        # must be greater than or equal to the value of the root
        # so we can do the same operation on the right side until
        # we reach a free space to create our node value.
        else:
            # if there is a child to the right
            if self.right:
                # run the insert method on that child
                self.right.insert(value)
            # if there is no child to the right
            else:
                # create the child to the right
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If theres no BST, return false
        if self.value is None:
            return False
        # if the target is equal to the self.value
        elif target == self.value:
            # the target exists
            return True
        # if the target is greater than the value
        elif target > self.value:
            # check for a right child
            if self.right:
                # if there is a right child, run contains on it
                return self.right.contains(target)
            # if there is no right child
            else:
            # then the target is not contained within
                return False
        # if the target is less than the comparison value
        elif target < self.value:
            # check for a left child
            if self.left:
                # run contains on the left child
                return self.left.contains(target)
            # re-assign the comparison value to the left child
            else:
            # run the contains method on that child
                return False

    """
    # chen's version of contains function

    # Return True if the Tree contains the value
    # false if it does not
    def contains(self, target):
        # base case: check self's value to see if it matches the target's
        if self.value == target:
            return True
        # otherwise we need to go either left or right
        # compare the target against self's value
        if target < self.value:
            # base case: if theres no node here, then the target is not in the tree
            if not self.left:
                return False
            # otherwise, there is a node there
            else:
            # call 'contains' on the left child
                return self.left.contains(target)
        else:
            # base case: if there's no node here, then the target is not in the tree
            if not self.right:
                return False
            # otherwise ther's a node there
            else:
            # call 'contains' on the right child 
                return self.right.contains(target)
    """
    """
    chen's revisit of get_max

    def get_max(self):
        # the max value is always going to be the right-most tree node
        # recursive version
        # if not self.right:
        #   return self.value
        # return self.right.get_max()

        # iterative version
        # current = self
        # while current.right:
        #   current = current.right
        # current doesnt have a right
        # return current.value
    """

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        # if it's not empty then it's automatically a node. check to the right
        # check for a right child
        elif self.right:
            # if there is a right child, run get_max again on that child
            return self.right.get_max()
        # if there is no right child
        else:
        # return the value
            return self.value
    """
    chen's revisit of the for_each
    # call the function 'fn' on the value of each node
    def for_each(self, fn):
        # recurse
        # call fn on self.value
        fn(self.value)
        # check if self has a left child
        if self.left:
            # call 'for_each' on the left child, passing in the fn
            self.left.for_each(fn)
        # check if self has a right child
        if self.right:
            # call 'for_each' on the right child, passing in fn
            self.right.for_each(fn)
        # This type of recursion is considered a Depth first Traversal
        # the function is traversing all the way down one route in one direction
        # before changing direction
        # depth first traversals are LIFO. They use stacks to traverse through


        #iterative version of depth first traversal
        stack = []
        # add the root node to our stack
        stack.append(self)
        # continue popping from our stack so long as there are nodes in it
        while len(stack) > 0:
            current_node = stack.pop()
            # check if this node has children
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

            fn(current_node.value)


    # Breadth First traversal
    from collections import deque
    q = deque()
    q.append(self)

    while len(q) > 0:
        current_node = q.popleft()

        # check if node has children
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)

        fn(current_node.value)

    # When the above finishes, it will have completed an iterative breadth first
    # traversal.
    """
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # apply function to first value
        fn(self.value)
        # if theres a left child
        if self.left:
            #recurse through it
            self.left.for_each(fn)
        # if there's a right child
        if self.right:
            # recurse through it
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()

            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            
            print(current_node.value)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []

        stack.append(self)
        
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

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
# """
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
