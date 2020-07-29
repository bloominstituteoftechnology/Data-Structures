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
        node = BSTNode(value)
        if value < self.value:
            # place to the left
            if self.left is None:
                self.left = node
            else:
                # recursion to apply insert on child
                self.left.insert(value)
        elif value >= self.value:
            # place to the right
            if self.right is None:
                self.right = node
            else:
                # recursion to apply insert on child
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target <= self.value:
            # search the left branch
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            # search the right branch
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # start with the first node (or current)
        current = self
        # look at the right-side ONLY, b/c left side is smaller
        if self.right is not None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    # go through all the nodes
    def for_each(self, fn):
        fn(self)
        pass

    # Extra/not needed
    def remove_node(self, target):
        # locate the node
        # if self.right -> replace node with self.right
        # if not self.right -> replace


        pass

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
