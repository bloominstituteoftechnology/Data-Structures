# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


# Binary Search Tree - discards duplicate values
class BinarySearchTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    # Insert the given value into the tree
    def insert(self, value):
        newNode = None
        if value < self.value:
            if self.left:
                newNode = self.left.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.left = newNode
        elif value > self.value:
            if self.right:
                newNode = self.right.insert(value)
            else:
                newNode = BinarySearchTree(value, self)
                self.right = newNode
        return newNode

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            else:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        return self.__getMaxNode().value

    def __getMaxNode(self):
        theMax = self
        if self.right:
            theMax = self.right.__getMaxNode()
        return theMax


    # Return the minimum value found in the tree
    def get_min(self):
        return self.__getMinNode().value

    def __getMinNode(self):
        theMin = self
        if self.left:
            theMin = self.left.__getMinNode()
        return theMin

    # 2) If right sbtree of node is NULL, then succ is one of the ancestors. Do following.
    # Travel up using the parent pointer until you see a node which is the left child of its parent. The parent of such a node is the succ.
    def getInorderSuccessor(self):
        node = self.__getInorderSuccessorNode()
        if node:
            return node.value
        else:
            return None

    def __getInorderSuccessorNode(self):
        if self.right:
            return self.right.__getMinNode()
        else:
            current = self
            parent = current.parent
            while current is not None and parent is not None and current != parent.left:
                parent = parent.parent
                current = current.parent
            return parent

    # 2) If left sbtree of node is NULL, then pred is one of the ancestors. Do following.
    # Travel up using the parent pointer until you see a node which is the right child of its parent. The parent of such a node is the pred.
    def getInorderPredecessor(self):
        node = self.__getInorderPredecessorNode()
        if node:
            return node.value
        else:
            return None

    def __getInorderPredecessorNode(self):
        if self.left:
            return self.left.__getMaxNode()
        else:
            current = self
            parent = current.parent
            while current is not None and parent is not None and current != parent.right:
                parent = parent.parent
                current = current.parent
            return parent

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
