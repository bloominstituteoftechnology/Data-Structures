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
        #check whether new nodes value is less than current nodes value
        if value < self.value:  
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # check weather new nodes value is greater or equal to current node
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False


    # Return the maximum value found in the tree
    def get_max(self):
        # The largest value will always be on the right of the current node
        #  if we can go right lets find the largest number by calling get_max on the right subtree
        #  of we cannot go right retrun the current value
        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree 
        if self.left:
            self.left.for_each(fn)
        #  if you can go right call for_each on the right tree
        if self.right:
            self.right.for_each(fn)

    # Part 2 ----------------------- Tree Traversal 

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
    def bft_print(self, node):
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            node = queue.get()
            print(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while not stack.isEmpty():
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

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

# bst.bft_print(bst)
# bst.dft_print(bst)

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
