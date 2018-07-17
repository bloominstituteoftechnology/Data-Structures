"""
BST is node-based
Left subtree contains only values less than node's value
Right subtree contains only values greater than node's value
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# param value is the data object to insert
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# First, compare value passed in with the node - > or <?
# If <, check left node. If nothing is there, congratulations - you have a
# new node.
# If something is there, insert the new value
# Same with the right.
# Ignore new value if equal to current node value

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False 
            else:
                return self.right.contains(target)
        return False

# If the target = the current value, we're done.
# If target > current value, look at left branch. If empty, return false.
# If not, call this function recursively on the branch
# If target < current value, do the same with the right branch
# If you don't find it anywhere, return false.
# NOTE:
# I got some help from a classmate who suggested the recursive function
# call to search. I was trying the find method and it wasn't working. The
# recursion works because the first 2 lines check on the current value and
# if it's true, then it returns True. It doesn't run forever because if
# there is nothing left to search, it returns False.


    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
			
# This works a little differently than linked lists because I'm pretty sure 
# the left branch, if it exists, is never going to contain the maximum, by
# definition. So you only need to check the right branch.
# I was looking at my linked list get_max as a model but I don't think 
# it'll work because we don't have a next_node here. So I think using 
# recursion again here makes sense.
# If there is nothing on the right branch, the current value must be the
# maximum
# If there is something there, then run the function recursively on itself.
# It will stop when there is nothing left on the right branch and return
# whatever value it currently holds as the maximum.
