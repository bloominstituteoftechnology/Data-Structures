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
        # Left side
        if value < self.value:
            if self.left:
                BSTNode(value)
            else:
                self.left = value
        # RIght side
        if value >= self.value:
            if self.right:
                BSTNode(value)
            else:
                self.right = value
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check root
        if target == self.value:
            return True
        #check subleft nodes:
        elif self.left.contains(target):
            return True
        #check subright nodes:
        elif self.right.contains(target):
            return True
        else: 
            return False
    # Return the maximum value found in the tree
    def get_max(self):
        # check if there is not a right(greater) value
        if self.right is None:
            max_val = self.value
        # traverse down list until no more right values are found
        else:
            self.right.get_max()

        return max_val
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        self.left.for_each(fn)
        self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        #define function to iterate without repitition for each condition
        def stack(n):
            #empty containers
            visited, s = [], [n]

            while s:
                n = s.pop()
                visited.append(n)
                #add right to stack first so that left pops first
                s.extend(filter(None, [n.right, n.left]))
            return visisted

        #check for empty tree
        if self.value is None:
            return None
        #if root is equal to node, traverse from here
        elif self.value == node.value:
            return stack(node)
        #search for starting node and traverse from there
        elif self.left is not None:
            current = self.left
            while current:
                if current = node:
                    return stack(node)
                elif current.left is not None:
                    current = current.Left
                else:
                    current = current.right
        elif self.right is not None:
            current = self.right
            while current:
                if current = node:
                    return stack(node)
                elif current.left is not None:
                    current = current.Left
                else:
                    current = current.right        
        else:
            return None

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
