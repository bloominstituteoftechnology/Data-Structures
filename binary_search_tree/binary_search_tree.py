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
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check to see if the value is greater than or equal to the value to the left
        if value < self.value and self.left is None:
            self.left = BSTNode(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value >= self.value and self.right is None:
            self.right = BSTNode(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # End Goal to return true: if the target value equals the self.value
        # than the tree contains the value.
        if target is self.value:
            return True

        # If the target is less than the value and the left value is NOT equal
        # to None, than we want to recursively run the contain method on the
        # self.left value.
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        
        # if the target is less than the self.value and the left value is None
        # than that means that the target is not contained in the tree
        elif target < self.value and self.left is None:
            return False

        # if the target is less than or equal to the self.value and the right value
        # is NOT equal to None, than we want to recursively run the contains method on
        # the self.right value
        elif target >= self.value and self.right is not None:
            return self.right.contains(target)

        # if the target is greater than or equal to the self.value and the 
        # right value is None, than the target is not contained in the tree.
        elif target >= self.value and self.right is None:
            return False

            

    # Return the maximum value found in the tree
    def get_max(self):
        # right values always increase in value as you go down the tree.
        # so if we just continue to search down the right, as long as the 
        # self.right is not None, than that value is our Max
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if self is None:
            return 
        if self is not None:
            if self.left:
                self.left.in_order_print(self)
            print(self.value)
            if self.right:
                self.right.in_order_print(self)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # refactor ideas... rather than increasing the size itterativly, we could use len()
        # or we could import the queue and the stack classes and use those...since they have the
        # size attribute, we could just call that attribute when done. 

        # # can use a queue...since queue we can remove the first items first
        # queue = []
        # queue.insert(0,node)
        
        # size = 1
        # # itterate thru the list...as long as the list size not equal to one
        # while size != 0:
        #     current_node = queue.pop()
        #     size -= 1
        #     print(current_node)
            
        #     # if there are nodes to the left and right of the parent node...then add those
        #     # to the queue...and increase the size of the queue. 
        #     if current_node.left:
        #         queue.insert(0, current_node.left)
        #         size += 1
        #     if current_node.right:
        #         queue.insert(0, current_node.right)
        #         size += 1

        queue = Queue()
        queue.enqueue(node)

        while queue.size > 0:

            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)

            if current_node.right:
                queue.enqueue(current_node.right)




                  

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        # using a stack for the depth...since the Last in is the first out...
        stack = []
        stack.append(node)

        

        # itterate thru the list as long as the list size does not equal 0
        while len(stack) != 0:
            current_node = stack.pop()
            
            print(current_node.value)

            if current_node.left:
                stack.append(current_node.left)

            if current_node.right:
                stack.append(current_node.right)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

if __name__ == "__main__":
    bst = BSTNode(1)
    
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)

    bst.bft_print(bst)