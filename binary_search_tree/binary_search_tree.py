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
        # if self.value is not None:
        #     cb(self.value)

        # if self.right:
        #     self.right.for_each(cb)
        # if self.left:
        #     self.left.for_each(cb)
        # return

        # depth first traversal
        stack = Stack()
        stack.push(self)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node=None):
        stack = Stack()

        stack.push(self)
        current_node = stack.pop()

        if current_node.left:
          #stack.push(current_node)
          return self.left.in_order_print(current_node)

        if current_node.right:
          #stack.push(current_node)
          return self.right.in_order_print(current_node)

        if stack.size == 0:
          return


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.size > 0:

          current_node = queue.dequeue()
          if current_node.left:
            queue.enqueue(current_node.left)
          if current_node.right:
            queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
          current_node = stack.pop()

        print(current_node)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(4)
bst.insert(3)
bst.insert(6)
bst.insert(10)
print(bst.value)  # 5
print(bst.left.value)  # 4
print(bst.left.left.value)  # 3
print(bst.right.value)  # 6
print(bst.right.right.value)  # 10
print(bst.contains(4))  # T
print(bst.contains(8))  # F
print(bst.contains(5))  # T
print(bst.contains(10))  # T


def printMe(x):
    print("PRINTME", x)


print(bst.for_each(printMe))

print("===")
print(bst.in_order_print())
print("===")
