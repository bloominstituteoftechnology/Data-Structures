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


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new < node.value 
        if value < self.value:
            # if left doesnt exist
            if self.left is None:
                # creat left
                self.left = BinarySearchTree(value)
            # else:
            else:
                # leftnode.insert value
                # we can't creat here
                # it will keep searching
                self.left.insert(value)
        #if >=
        else:# value is greater than or equal to
            # if right doesnt exist
            if self.right in None:
                # creat right
                self.right = BinarySearchTree(value)
            else:
                self.righ.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching self would be the root
        # compare the traget against self

        # criteria for returning False: we know we need to go in one direction
        # but threr's nothing in the left or right direction


        if target == self.value:
            return True
        if target < self.value: 
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if left is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)
        
            

    # Return the maximum value found in the tree1
    def get_max(self):
        # if there's a right:
        if self.right:
            #  get max on right
            return self.right.get_max()
        # else:
        else:
            # return node. value
            return self.value   

    def  iter_get_max(self):
        current_max = self.value

        current = self
        # traverse our structure
        while current is not None:
            if current.value> current_max:
                current_max = current.value
            # update our current_max variavle if we see a larger value
            current = current.right
        return current_max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        # so here we need to call function if the nodes are there 
        # pass this function tho the left child
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child
        if self.righ:
            self.right.for_each(fn) 
    
    
    def iter_for_each(self, fn):
        stack = []
        
        #add the root node
        stack.append(self)

        #loop so long as the stack still has elemnts
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(currnet.right)
            if current.left:
                stack.append(current.left)
            fn(current.value)
    # Depth-First traversal


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
