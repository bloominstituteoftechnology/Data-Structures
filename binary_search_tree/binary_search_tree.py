from collections import deque

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
        # check whether new node's value is less than current node's value
        if value < self.value:
            # if there's nothing left of current node
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value >= target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value is less than target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # U: traverse BST to find global max
        # 1. check your input --> is there a node here?
        # 2. declare max variable == self.val
        # 3. iterate through tree until we hit Null
        # 4. update max val
        # 5. move to the right
        if not self.right:
            return self.value
        return self.right.get_max()

    # recursive solution
    # base case: no right node available
    # recursive step: pass right subtree to get_max

    # Call the function `fn` on the value of each node
    # fn = anonymous function or lambda function
    def for_each(self, fn):
        # U: apply fn to each node of tree
        if self.left:
            self.left.for_each(fn)

        fn(self.value)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        # preorder? left -> root -> right
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # 1. define deque
        # 2. add self to deque
        # 3. iterate: while there are items in the deque
        # 4. dequeue/pop from deque and point to result, and print
        # 5. add left and right children to deque

        qq = deque()
        qq.append(self)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = []
        s.append(self)

        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    # check self
    # 1. print self
    # root -> left -> right
    # 2. recurse to the left
    # 3. recurse to the right

    # Print Post-order recursive DFT
    # def post_order_dft(self):
    # 0. check self
    # 1. print self
    # left -> right -> root
    # 2. recurse to the left
    # 3. print self


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

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_dft()
