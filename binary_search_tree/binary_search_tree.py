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
        # check if value is int
        value_type = type(value)
        if value_type != int and value_type != float:
            print(f"Error: Insert type is {value_type}")
            print("type must be 'int'")
            return
        # check if the value is Less than the value of the current node's value
        if value < self.value: 
            # if there's no left child already there
            if not self.left:
                # add the new node to the left
                left_node = BSTNode(value)
                # create a BSTNode and encapsulate the value in it and then set it to the Left node
                self.left = left_node
            # otherwise recursively call insert on left node
            else:
                self.left.insert(value)
        # otherwise the value is Greater than or Equal to the value of the current node
        elif value >= self.value:
            # if there's no right child already there
            if not self.right:
                # add the new node to the right
                right_node = BSTNode(value)
                # create a BSTNode and encapsulate the value in it and then set it to the Right node
                self.right = right_node
            # otherwise recursively call insert on right node
            else:
                self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if target == self.value:
            # return True
            return True
        # check if the target is Less than the value of the current node's value
        elif target < self.value:
            # if there's no left child already there
            if not self.left:
                # return False
                return False
            # otherwise
            else:
                # return a call of 'contains' on the Left child passing in the target value
                return self.left.contains(target)
        # otherwise the target is Greater than to the value of the current node
        elif target > self.value:
            # if there's no Right child already there
            if not self.right:
                # return False
                return False
            # otherwise
            else:
                # return a call of 'contains' on the Right child passing in the target value
                return self.right.contains(target)
        else:
            print(f"Could not search tree for {target}")
        

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty Tree
        if not self.value:
            # return None
            print("empty tree")
            return None

        # ** EASY - Recursive **
        # check if there is no node to the Right
        if not self.right:
            # if True return value
            return self.value
        # otherwise return a call to get_max on the Right child
        else:
            return self.right.get_max()

        # ** ITERATIVE approach **
        # initialize the max value //self's value
        # get a ref to the current node
        # Loop while there is still a Node
            # if the current value is greater than the max value, update the max value
            # move onto the next right node

        # return max value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function passing in the current node's value
        fn(self.value)
        # if there is a node to the Left
        if self.left:
            # call the function on the Left value
            self.left.for_each(fn)
        # if there is a node to the Right
        if self.right:
            # call the function on the Right value
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
bst = BSTNode(4)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert("2")

print(bst.contains(6))
print(bst.contains(56))

print(bst.get_max())

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
