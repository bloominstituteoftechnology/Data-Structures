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
# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         #First: Case 1 Value is less thean self.value --> goes left
#         if value < self.value:
#             #if no left child, insert value here
#             if self.left is None:
#                 self.left = BSTNode(value)
              
                
#             #else repeat the process on left subtree
#             #self.left.insert(value) --> recursion
#             else:
#                   self.left.insert(value)
                
                

#         #Case2 value is greater than self.value --> goes right
#         #Case3 value is equal to self.value --> usally goes right (in solution d/t tests goes right)
        
#         #First: Case 1 Value is less thean self.value --> goes left
#         elif value >= self.value:
#             #if no left child, insert value here
#             if self.right is not None:
#                 self.right.insert(value)
                
#             #else repeat the process on left subtree
#             #self.left.insert(value) --> recursion
#             else:
#                 self.left = BSTNode(value)
                
#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         # Case 1: self.value is equal to the target
#         if self.value == target:
#             return True
#         #Case 2: If target is less than self.value
#         if target < self.value:
#             #if self.left is none it isn't in the tree
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.contains(target) #Recursive call --> must return on contains, not needed on insert
#         #Case 3: otherwise
#         else:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.contains(target)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    #Return True if the tree contains the value
    #False if is doesn't

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
            fn(self.value)
            if self.right is not None:
                self.right.for_each(fn)
            if self.left is not None:
                self.left.for_each(fn)
            return
       

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)

        if node.right is not None:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversals
    def bft_print(self, node):
        #create a queue
        #add the first node to the queue
        #while queue is not empty
            #remove the first node in queue
            #print the removed node
            #add all children into queue
        que_class = Queue()
        que_class.enqueue(node)
        while que_class.size > 0:
            head = que_class.storage[0]
            print(head.value)
            que_class.dequeue()
            if head.left != None:
                que_class.enqueue(head.left)
            if head.right != None:
                que_class.enqueue(head.right)
            


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create a stack fo nodes
        #add the first node to the stack
        #while the stack is not empty
            #get the current the current node from the top of the stack
            #print that node
            #add all children to the stack, keep in mind order matters
        
        stack_class = Stack()
        stack_class.push(node)
        while stack_class.size > 0:
            current = stack_class.pop()
            print(current.value)
            if current.left is not None:
                stack_class.push(current.left)
            if current.right is not None:
                stack_class.push(current.right)
           

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

BST = BSTNode(1)
BST.insert(8)
BST.insert(5)
BST.insert(7)
BST.insert(6)
BST.insert(3)
BST.insert(4)
BST.insert(2)

BST.dft_print(BST)