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


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False
        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.remove_head()
        else:
            return None


class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.remove_tail()
        else:
            return None


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
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    # iterative
    def contains(self, target):
        node = self
        while node != None:
            if target > node.value:
                node = node.right
            elif target < node.value:
                node = node.left
            else:
                return True
        return False

    # Return the maximum value found in the tree
    # recursive
    # def get_max(self):
    #     if self.right:
    #         return self.right.get_max()
    #     else:
    #         return self.value

    # iterative
    def get_max(self):
        node = self
        highest = node.value
        while node != None:
            highest = node.value
            node = node.right
        return highest

    # Call the function `fn` on the value of each node
    # recursive
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # iterative
    # def for_each(self, fn):
    #     pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # First check if there is a node to the left, if so prioritize executing this function on that node first
        if node.left:
            node.left.in_order_print(node.left)
        # Then visit the current node on the current function call
        print(self.value)
        # Then check if there is a node to the right, and if so, call this function on that node and it's children
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Create the queue and add the first node
        print_queue = Queue()
        print_queue.enqueue(node)

        # While the queue is greater than zero
        while print_queue.size > 0:

            # The current node equals the first item in the queue, and the item is removed from the front of the queue
            current_node = print_queue.dequeue()
            # Do whatever it is you must do to the node, visit, check for base condition, execute callback, modify value, etc.
            print(current_node.value)

            # If there is a left node add it to the end of the queue
            if current_node.left:
                print_queue.enqueue(current_node.left)
            # If there is a right node add it to the end of the queue
            if current_node.right:
                print_queue.enqueue(current_node.right)

            # Now the next node in the current row will be up first in the queue
            # and the next row will be lined up in order from left to right after the items in the current row

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # Create the stack and add the first node
        print_stack = Stack()
        print_stack.push(node)

        # While the stack length is greater than zero
        while print_stack.size > 0:

            # Change the current node to node on the top/end of the stack, and remove that node from the top of the stack
            current_node = print_stack.pop()
            # Do whatever it is you must do to the node, visit, check for base condition, execute callback, modify value, etc.
            print(current_node.value)

            # If there is a left node add it to the top of the stack
            if current_node.left:
                print_stack.push(current_node.left)
            # If there is a right node add it to the top of the stack
            if current_node.right:
                print_stack.push(current_node.right)

            # Now the left node beneath the current node will be up next, on top of the stack
            # and if that first node has another node to the left below it, that will be placed on the stack
            # the stack will only get to the right current node once the full extent of left nodes has been visited
