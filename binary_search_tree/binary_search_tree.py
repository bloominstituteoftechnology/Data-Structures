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

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        output_list = []
        self.for_each(lambda x: output_list.append(x))

        [print(x) for x in sorted(output_list)]

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        from collections import deque
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    # helper function to do the actual work
    def pre_order_func(self):

        output_list = []
        output_list.append(self.value)

        if self.left:
            output_list.extend(self.left.pre_order_func())
        if self.right:
            output_list.extend(self.right.pre_order_func())

        return output_list

    def pre_order_dft(self):
        
        output_list = self.pre_order_func()

        [print(x) for x in output_list]

    def post_order_func(self):

        output_list = []
        if self.left:
            output_list.extend(self.left.post_order_func())
        if self.right:
            output_list.extend(self.right.post_order_func())

        output_list.append(self.value)

        return output_list

    # Print Post-order recursive DFT
    def post_order_dft(self):
        
        output_list = self.post_order_func()

        [print(x) for x in output_list]

if __name__=='__main__':
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
