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
        ## case 1 : value is less than self.value
        if value < self.value:
            # if there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
             # else insert()
             ## RECURSION!!!!
                self.left.insert(value)

        ## case 2: value is greater than or equal to self.value
        elif value >= self.value:
            # if there is no left child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
             # else insert()
             ## RECURSION!!!!
                self.right.insert(value)
        #pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        #pass

    # Return the maximum value found in the tree
    def get_max(self):
        ## forget about the left subtree
        ## iterate through the nodes using a loop construct
        
        # max_value = self.value
        # #print(f'max value {max_value}')
        # if self.right == None:
        #     # print(f"right node{self.right}")
        #     # print(f"MAX VALUE: {max_value}")
        #     # #max_value = self.value
        #     # print("PASSSSSS")
        #     final_max_value = self.value
        #     #print(f"FINAL MAX VALUE: {max_value}")
        #     return final_max_value
            
        # elif self.right.value > max_value:
        #     #print(f'right node value: {self.right.value}')
        #     max_value = self.right.value
        #     #print(f'new max value: {self.right.value}')
        #     v = self.right.get_max()
        #     return v
        # #print(f'final returned max value {final_max_value}')
        # #return final_max_value
        #----------

        if self.right == None:
            return self.value
        
        return self.right.get_max()



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        ## recursive solution
        #print(self.value)
        #print(self.left)
        #print(self.right.value)
        fn(self.value)

        #current _value = self.value
        #print(f'self value: {self.value}')

        ### THE LEFT TREE
        if self.left == None:
            pass
        #print("Pass on the left")
        else:
            #print(f'left node: {self.left.value}')
            self.left.for_each(fn)


        if self.right == None:
            pass
            #print("Pass on the right")
        else: 
            #print(f'right node: {self.right.value}')
            self.right.for_each(fn)






    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
       
        if self is None:
            return

        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(node)

        #visit the OG node by printing its value
        print(self.value)

        # check if we can move right

        if self.right is not None:
            self.right.in_order_print(node)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #use a queue to form a line for the nodes to get in
        #start by placing the root in the queue
        queue = Queue()
        queue.enqueue(node)
    
        # need a while loop to iterate
        # in while statement, check length of queue
        #while length of queue is > 0
        while (queue.size()) > 0:
    
            #dequeue item from front of queue
            #print item
            current_item = queue.dequeue()
            print(current_item.value)

            #place current item's left node in queue if not None
            if current_item.left is not None:
                queue.enqueue(current_item.left)
            #place current item's right node in queue if not None
            if current_item.right is not None:
                queue.enqueue(current_item.right)




    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        stack.push(node)

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while (stack.size()) > 0:
            # pop top item off the stack
            top_item = stack.pop()
            # print that item's value
            
            print(top_item.value)


            # if there is a right subtree
                # push right item onto the stack
            if top_item.right is not None:
                stack.push(top_item.right)
            # if there is a left subtree
                # push left item onto the stack
            if top_item.left is not None:
                stack.push(top_item.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        #current-left-right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


## Queue
class Queue:
    def __init__(self):
        self.storage = []
    
    def __len__(self):
        return len(self.storage)
        #pass

    def size(self):
        return len(self.storage)

    def enqueue(self, value):
        
        return self.storage.insert(0, value)
        #pass

    def dequeue(self):
        if len(self.storage) >= 1:
            return self.storage.pop(-1)

class Stack:
    def __init__(self):
        #self.size = 0
        ## array is the underlying data structure
        self.storage = []

    def __len__(self):
        return (len(self.storage))
       #pass

    def size(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)
        #pass

    def pop(self):
        if len(self.storage) >= 1:
            return self.storage.pop()