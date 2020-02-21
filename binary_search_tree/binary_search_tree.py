from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None  # left_LESS_subtree
        self.right = None  # right_GREATER_EQUAL_subtree

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            if self.value > value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif self.value < value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
                if not self.left or self.left.value is None:
                    return False
                elif self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            elif self.value < target:
                if not self.right or self.right.value is None:
                    return False
                elif self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # depth first traversal - recursive
        if self.value is not None:
            cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        return

        # depth first traversal - iterative
        # stack = Stack()
        # stack.push(self)

        # while stack.len() > 0:
        #     current_node = stack.pop().value
        #     cb(current_node.value)
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """
    Breadth First Traversal
    Make a queue
    Put root in the queue
    While queue is not empty
      pop out front of queue
      DO THE THING!
      if left:
        add left to back of queue
      if right:
        add right to back of queue
    """

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current_node = queue.dequeue().value
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    """
    Depth First Traversal
    Make a stack
    put root in stack
      while stack not empty
      pop root out of stack
      DO THE THING!!!!
      if left
          add left to stack
      if right
          add right to stack
    """

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop().value
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)
print(bst.value)  # 8
print(bst.left.value)  # 3
print(bst.right.value)  # 10

print(bst.contains(8))  # T


def printMe(x):
    print("PRINTME", x)


print(bst.for_each(printMe))

print("===")
print(bst.dft_print(bst))
print("===")

print("===")
print(bst.bft_print(bst))
print("===")

print("===")
print(bst.in_order_print(bst))
print("===")
