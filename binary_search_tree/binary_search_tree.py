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
        new = BSTNode(value)
        node = self
        def traverse(node, new):
            if node.left == None and new.value < node.value:
                node.left = new
                return
            if new.value < node.value:
                traverse(node.left, new)
            if node.right == None and new.value >= node.value:
                node.right = new
                return
            if new.value >= node.value:
                traverse(node.right, new)
        traverse(node, new)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        def search(node, target):
            if node == None:
                return False
            if node.value == target:
                return True
            elif target < node.value:
                return search(node.left, target)
            else:
                return search(node.right, target)
            
        return search(node, target)

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        def right_traverse(node):
            if node.right == None:
                return node.value
            return right_traverse(node.right)
        return right_traverse(node)

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        node = self
        self.fn = fn
        def traverse(node):
            if node == None:
                return
            self.fn(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(node)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        node = self
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            print(node.value)  
            traverse(node.right)
  
        traverse(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        node = self
        prev = node
        def traverse(node, prev):
            while node != None:
                print(node.value)
                if node.left != None:
                    prev = node
                    node = node.left
                else:
                    node = prev.right
                    prev = node
        traverse(node, prev)
        traverse(node.right, prev)
      
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
bst = BSTNode(8)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(2)

bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)

# bst.in_order_print()
bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
