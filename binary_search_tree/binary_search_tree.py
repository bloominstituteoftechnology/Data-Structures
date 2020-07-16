import random
"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

O(log n): halving with every single iteration

Left Child must be < Parent
Right Child must be > Parent
Note: Keep hierarchy in mind; rule applies throughout tree

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

    def insert(self, value):
        """
        Insert the given value into the tree
        """
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see there is no left child,
            if self.left is None:
                # then we can wrap the value in a BSTNode and
                # park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        if value >= self.value:
            # we need to go right
            # if we see there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and
                # park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    def contains(self, target):
        """
        Return True if the tree contains the value
        False if it does not
        """
        # Compare input value with value of the node
        # if value == Node's value
        if target == self.value:
            # return True
            return True
        else:
            # if value < Node's value
            if target < self.value:
                # if there is no right child
                if self.left is None:
                    # tree does not contain value
                    return False
                else:
                    # call the left child's `contains` method
                    return self.left.contains(target)
            # if value > Node's value
            if target > self.value:
                # if there is no right child
                if self.right is None:
                    # tree does not contain value
                    return False
                else:
                    # call the right child's `contains` method
                    return self.right.contains(target)

    def get_max(self):
        """
        Return the maximum value found in the tree
        """
        # Inspect root node
        max_val = self.value
        # Check for children
        if self.right is None:
            return max_val
        else:
            # Check if right child value is < Node value
            if self.right.value < max_val:
                return max_val
            else:
                max_val = self.right.value
                # call the right child's `get_max` method
                return self.right.get_max()

    def for_each(self, fn):
        """
        Call the function `fn` on the value of each node
        """
        # fn(root.value)
        # Start with root (no children)
        if self.left is None and self.right is None:
            return fn(self.value)
        else:
            # Handle both sides when not None
            if self.left is not None and self.right is not None:
                return fn(self.value), self.left.for_each(
                    fn), self.right.for_each(fn)
            # Hande right side
            if self.right is not None and self.left is None:
                return fn(self.value), self.right.for_each(fn)
            # Handle left sides
            if self.left is not None and self.right is None:
                return fn(self.value), self.left.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # add the current node's right child first (for left to right
            # order)
            if current.right:
                stack.append(current.right)

            # add the current node's left child
            if current.left:
                stack.append(current.left)

            # call the anonymous function
            fn(current.value)


    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        
        # BFT: FIFO
        # we'll use a queue to facilitate the ordering
        queue = deque()
        queue.append(self)

        # continue to traverse so long as there are nodes
        # in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            fn(current.value)



    # Part 2 -----------------------

    
    def in_order_print(self, node):
        """
        Print all the values in order from low to high
        Hint:  Use a recursive, depth first traversal
        """
        # Use a stack to guide traversal        
        stack = []
        stack.append(self)

        vals = set()

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()
            vals.add(current.value)

            # add the current node's right child first (for left to right
            # order)
            if current.right:
                vals.add(current.right.value)
                stack.append(current.right)

            # add the current node's left child
            if current.left:
                vals.add(current.left.value)
                stack.append(current.left)

        # Need to print each value from low to high
        for i in sorted(list(vals)):
            print(i)

    
    def bft_print(self, node):
        from collections import deque
        """
        Print the value of every node, starting with the
        given node, in an iterative breadth first traversal.
        layers, FIFO
        """
        # Use a queue to guide traversal        
        queue = deque()
        queue.append(self)

        vals = []
        vals.append(self.value)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(queue) > 0:
            # pop the top node from the stack
            current = queue.popleft()

            # check for children

            # add the current node's right child first (for left to right
            # order)
            if current.right: # and current.left is None:
                vals.append(current.right.value)
                queue.append(current.right)

            # add the current node's left child
            if current.left: # and current.right is None:
                vals.append(current.left.value)
                queue.append(current.left)

        # Need to print each value
        for i in vals:
            print(i)


    def dft_print(self, node):
        """
        Print the value of every node, starting with the
        given node, in an iterative depth first traversal.
        LIFO
        """
        # Use a stack to guide traversal        
        stack = []
        stack.append(self)

        vals = []
        vals.append(self.value)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop(0)
            print("Stack size:", len(stack))
            print("Current:", current.value)

            # check for children

            # add the current node's right child first (for left to right
            # order)
            if current.right: # and current.left is None:
                vals.append(current.right.value)
                stack.append(current.right)

            # add the current node's left child
            if current.left: # and current.right is None:
                vals.append(current.left.value)
                stack.append(current.left)

            # # if both children exist
            # if current.right and current.left:
            #     vals.append(current.right.value)
            #     stack.append(current.right)

        # Need to print each value
        for i in vals:
            print(i)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


if __name__ == "__main__":

    print("---" * 5 + "INSERT TEST" + "---" * 5)
    root = BSTNode(5)
    root.insert(2)
    root.insert(3)
    root.insert(7)
    root.insert(6)
    print(root.left.right.value)  # > 3
    print(root.right.left.value)  # > 6

    # breakpoint()

    print("---" * 5 + "CONTAINS TEST" + "---" * 5)
    root = BSTNode(5)
    root.insert(2)
    root.insert(3)
    root.insert(7)
    print(root.contains(7))  # > True
    print(root.contains(8))  # > False

    # breakpoint()

    print("---" * 5 + "GET_MAX TEST" + "---" * 5)
    root = BSTNode(5)
    print(root.get_max())  # > 5
    root.insert(30)
    print(root.get_max())  # > 30
    root.insert(300)
    root.insert(3)
    print(root.get_max())  # > 300
    print("---" * 15)

    # breakpoint()

    print("---" * 5 + "FOR_EACH TEST" + "---" * 5)
    root = BSTNode(5)
    arr = []
    def cb(x): return arr.append(x)

    v1 = random.randint(1, 101)
    v2 = random.randint(1, 101)
    v3 = random.randint(1, 101)
    v4 = random.randint(1, 101)
    v5 = random.randint(1, 101)

    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)
    print("v4:", v4)
    print("v5:", v5)

    root.insert(v1)
    root.insert(v2)
    root.insert(v3)
    root.insert(v4)
    root.insert(v5)

    root.for_each(cb)

    # breakpoint()

    print("5:", 5 in arr)
    print("v1:", (v1 in arr))
    print("v2:", (v2 in arr))
    print("v3:", (v3 in arr))
    print("v4:", (v4 in arr))
    print("v5:", (v5 in arr))
    print("---" * 15)

    print("---" * 5 + "TRAVERSALS TEST" + "---" * 5)
    root = BSTNode(1)
    root.insert(8)
    root.insert(5)
    root.insert(7)
    root.insert(6)
    root.insert(3)
    root.insert(4)
    root.insert(2)

    # print("DFT Print:", root.dft_print(root))
    breakpoint()