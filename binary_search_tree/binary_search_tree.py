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
            if self.left:
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            return self.left.contains(target) if self.left else False
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return True

    # Return the maximum value found in the tree

    def get_max(self):
        return self.right.get_max() if self.right else self.value

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
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    
    def bft_print(self, node):
        pass
        
        # enqueue the first node
        # queue.enqueue(node)

        # while there are nodes in queue:
            # process the first node by first dequeuing
            # then print the node's value (work first)
            # then enqueue it's childeren

        # while len(queue) > 0:
        #     next_node: BSTNode = queue.dequeue()
        #     print(next_node.value)
        #     if next_node.left:
        #         queue.enqueue(next_node.left)
        #     if next_node.right:
        #         queue.enqueue(next_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        
        # stack = Stack()

        # stack.push(node)
              
        # while len(stack) > 0:
        #     next_node: BSTNode = stack.pop()
        #     print(next_node.value)
        #     if next_node.left:
        #         stack.push(next_node.left)
        #     if next_node.right:
        #         stack.push(next_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
