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
        self.length = 0
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Recursive Edition
        # start at root and loop until condition is met
        # if value < self.value and self.left is None:
        #     self.left = BSTNode(value)
        #     return
        # elif value >= self.value and self.right is None:
        #     self.right = BSTNode(value)
        #     return
        # elif value < self.value:
        #     self.left.insert(value)
        # else:
        #     self.right.insert(value)

        # Non-Recursive Edition
        # print('self', self.value)
        current_node = self

        while current_node is not None:
            # print('current_node', current_node.value)
            if value <= current_node.value:
                if current_node.left is None:
                    current_node.left = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    # print('left child', current_node.left.value)
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BSTNode(value)
                    current_node.length += 1
                    return
                else:
                    # print('right child', current_node.right.value)
                    current_node = current_node.right

    
    def delete(self, value):
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self

        while current_node is not None:
            if target < current_node.value:
                if current_node.left is None:
                    return False
                else:
                    # print('left child', current_node.left.value)
                    current_node = current_node.left
            elif target > current_node.value:
                if current_node.right is None:
                    return False
                else:
                    # print('right child', current_node.right.value)
                    current_node = current_node.right
            else:
                return True

        # if target is == to current we return true
        # if target is < current we go left
        # if > we go right
        # if target reaches a leaf and it cant go left or right return 'target does not exist'

    # Return the maximum value found in the tree
    def get_max(self):
        # go right
        current_node = self

        while current_node is not None:
            if current_node.right is None:
                return current_node.value
            else:
                current_node = current_node.right

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self is None:
            return
        else:
            print('self', self.value)
            # print('self.left', self.left.value)
            # print('self.right', self.right.value)
            left_tree = BSTNode.for_each(self.left, fn)
            right_tree = BSTNode.for_each(self.right, fn)
            return fn(self.value)
            

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

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
