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
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # Create the Node from the value
        new_node = Node(value)

        if self.head is None and self.tail is None:
            # have both head and tail refer to a single node
            self.head = new_node
            self.tail = new_node
        else:
            # set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            self.tail = None
            return head.get_value()

        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None:
            return

        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        #set the tail to be None
        val = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        # remove new tail's reference to the old tail
        self.tail.set_next(None)
        return val

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at
        current = self.head

        # check to see if we're at a valid node
        while current:
            # return True if the current value we're lookin at matches our target value
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
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # returns the number of elements in the queue
        return self.size

    def enqueue(self, value):
        # We increment it by 1
        self.size += 1
        # This adds the element to the back of the queue
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # if the 'size' is greater than 1
        if self.size > 0:
            # decrement the 'size' by 1
            self.size -= 1
            # remove and return the element at the front of the queue
            return self.storage.remove_head()
        return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # returns the number of elements in the stack
        return self.size

    def push(self, value):
        # increment the size by 1
        self.size += 1
        # add the item to the top of the stack
        return self.storage.add_to_tail(value)

    def pop(self):
        # if the size is greater than 0
        if self.size > 0:
            # decrement by 1
            self.size -= 1
            # removes and return the element at the top of the stack
            return self.storage.remove_tail()
        return None

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node.
            # if value < Node's value, we need to go left
            if value < self.value:
                 # if we see that there is no left child
                 if self.left is None:
                    # then we can wrap the value in a BSTNode and park it
                    self.left = BSTNode(value)
                 # otherwise if there is a child
                 else:
                # call the left child's 'insert' method
                    self.left.insert(value)
            # if value >= Node's value, we need to go right
            else:
                # we need to go right if we see there is no right child
                if self.right is None:
                    # then we can wrap the value in a BSTNode and park it
                    self.right = BSTNode(value)
                # otherwise if there is a child
                else:
                    # call the right child's 'insert' method
                    self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the node matches the value of the target, we found what we're looking for
        if target == self.value:
            return True

        # compare the target against this node's value to determine which direction to go in
        if target < self.value and self.left:
            return self.left.contains(target)

        # if the value isn't on the left, then we check to see if we can go right
        if self.right:
            return self.right.contains(target)

        # if both conditions fail, then the value isn't in the tree
        return False 

    # Return the maximum value found in the tree
    def get_max(self):
        # node = self.right

        # while node:
        #     if node.right:
        #         node = node.right
        #     else:
        #         break
        # return node and node.value or self.value

        # the max value in the tree will always be the right-most value
        # we'll just keep going right until there is no right child
        # base case: there is no right child
        if not self.right:
            return self.value
        # otherwise, call 'get_max' on the right child
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the anonymous function on 'self.value'
        fn(self.value)

        # if this node has a left child
        if self.left:
            # pass the anonymous fn to it
            self.left.for_each(fn)
        
        # if this node has a right child
        if self.right:
            # pass the anonymous fn to it
            self.right.for_each(fn)


    def iterative_depth_first_for_each(self, fn):
        #DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it, there's more nodes to traverse
        while len(stack) > 0:
            current = stack.pop()

            # add the current node's right child first
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

        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

                fn(current.value)

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
        queue = Queue()
        queue.enqueue(node)
        while queue.__len__() > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while stack.__len__() > 0:
            node = stack.pop()

            print(node.value)

            if node.left:
                stack.push(node.left)

            if node.right:
                stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
