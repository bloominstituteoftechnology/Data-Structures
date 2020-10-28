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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self, index=0):
        if len(self.storage) == 0:
            return None
        self.size -= 1
        return self.storage.pop(index)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if len(self.storage) == 0:
            return None
        self.size -= 1
        return self.storage.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        cur_node = self
        new_node = BSTNode(value)

        # print('new.value: ' + str(new_node.value))
        # print('self.value: ' + str(cur_node.value))

        while True:
            if new_node.value >= cur_node.value:
                if cur_node.right is None:
                    # print('values:right: ' + str(cur_node.value))
                    cur_node.right = new_node
                    break
                cur_node = cur_node.right
            elif new_node.value < cur_node.value:
                if cur_node.left is None:
                    # print('values:left: ' + str(cur_node.value))
                    cur_node.left = new_node
                    break
                cur_node = cur_node.left
            else:
                print('value already in tree')
                break

        # RECURSIVE
        # if value is < root, go left
            # if left child is None:
                # add here.... left child = BSTNode(value)
            # else
            #    self.left.insert(value) # recursive call

        # if value >= root, go right (dupes go to the right)
            # if right child is None
                # add here
            # else
            #    self.right.insert(value) # recursive call

        # ITERATIVE
        # while not at bottom level of tree
            # if value is < root, go left
             # if left child is None:
                # add here
                # exit loop

            # if value >= root, go right (dupes go to the right)
                # if right child is None
                # add here
                # exit loop

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if self.value is target
        # if yes, return true
        # if no,
        # go left
        # go right
        cur_node = self

        while True:
            if target == cur_node.value:
                return True
            elif target > cur_node.value:
                if cur_node.right is None:
                    return False
                cur_node = cur_node.right
            elif target < cur_node.value:
                if cur_node.left is None:
                    return False
                cur_node = cur_node.left
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you cannot anymore
        # return value at far right
        cur_node = self
        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        # base case - no chidlren
        if self.left is None and self.right is None:
            return

        # recursive case - 1 or more children
        # go left, call fn(value) for each node
        if self.left:
            self.left.for_each(fn)
        # go right, call fn(value) for each node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        # Recursive - place your print statement
        # that explore left & right subtrees

        if self.left is None and self.right is None:
            print(self.value)
            return

        # recursive case - 1 or more children
        # go left, call fn(value) for each node
        if self.left:
            self.left.in_order_print()
        print(self.value)
        # go right, call fn(value) for each node
        if self.right:
            self.right.in_order_print()

        # Interative - think abou the order in which we are adding ndoes to the stack

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # breadth-first
        # visit all nodes at the same level first
        # level-order traversal
        # Create a Queue to keep track of nodes
        # insert self onto beginning of Queue
        # while something still in Queue
        # add left and right if exist to the queue
        # print and remove first node

        q = Queue()
        q.enqueue(self)
        print(f"queue lenght: {q.__len__()} ")
        # for i in q.storage:
        #     print(f"i is: {i.right.value} ")

        while(q.size != 0):
            for i, node in enumerate(q.storage):
                print(node.value)
                # print(q.storage[0].value)
                if node.left is not None:
                    q.enqueue(node.left)
                    # print(f"queue lenght:left:before {q.__len__()} ")
                    # q.dequeue()
                    # print(f"queue lenght:left:after {q.__len__()} ")
                if node.right is not None:
                    q.enqueue(node.right)
                    # print(f"queue lenght:right:before {q.__len__()} ")
                    # q.dequeue()
                    # print(f"queue lenght:right:after {q.__len__()} ")
                # if node.left is None and node.right is None:
                # print(f"queue lenght:none:before {q.__len__()} ")
                q.dequeue(i)


        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self):
        # depth-first
        # visit all the children first, then go to the next children
        # create a stack to keep track of nodes we are procssing
        # push root into stack

        # while something still in the stack (not done processign all nodes)
        # use existing 'for_each()' as a reference for traversal logic
        # push when we START, pop when a node is DONE
        # and don't forget to call 'print()'
        s = Stack()
        s.push(self)
        print(f"length is: {s.__len__()} ")
        while(s.__len__() != 0):
            for node in s.storage:
                if node.left is None:
                    if node.right is not None:
                        s.push(node.right)
                if node.left is not None:
                    s.push(node.left)
                    if node.right is not None:
                        s.push(node.right)
                print(node.value)
            s.pop()
            return

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):

        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""

# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)

# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

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

# print(bst.contains(-10))

print("bft order:")
bst.bft_print()

print("dft order:")
bst.dft_print()


# def bft_print(self):
#         q = Queue()
#         q.enqueue(self)
#         while(q.size != 0):
#             for i, node in enumerate(q.storage):
#                 print(node.value)
#                 if node.left is not None:
#                     q.enqueue(node.left)
#                 if node.right is not None:
#                     q.enqueue(node.right)
#                 q.dequeue(i)