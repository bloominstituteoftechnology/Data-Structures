from collections import deque

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
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            #if the value is less than the current value (meaning it needs to go on the left)
            #if there is nothing on the left, we can just plop it in there,
            #it has reached the correct spot on the tree
            if not self.left:
                self.left = BinarySearchTree(value)
            #even though the value was less than the current value, if there is something
            #already to the left, we need to use the insert function to see if that is greater
            #or less than our value
            else:
                return self.left.insert(value)
        else:
            #rinse and repeat above notes 
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # we always start searching at the root
        # compare the target against the self(node)

        #criteria for returning False:
        # we know we need to go in a direction, but we have reached the end, there is nothing there
        
        if target == self.value:
            return True
        if target < self.value:
            #go left if target is smaller than the current value
            if not self.left:
                #if we can't go left, then our value isn't here
                return False
            return self.left.contains(target)
        else: 
            #go right if target is larger than current
            if not self.right:
                #if we have reached a point w/o a right node, the value isnt here
                return False
            #we have to keep checking the next value, intro recursion
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # lesson code

        #we just gotta keep going right
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

        # end lesson code

        #this was more complicated than necessary because
        #I just need to go right until it runs out, as the largest
        #value will be furthest to the right

        # if self.right: 
        #     if self.value >= self.right.value:
        #         return self.value
            
        #     if self.value < self.right.value:
        #         return self.right.get_max()
        # else:
        #     return self.value

    def iterative_get_max(self):
        # 
        current_max = self.value
        # traverse the structure & update current max variable

        while self:
            if self.value > current_max:
                current_max = self.value
                #always go right bc the largest value always on the right
                #then just go until it ends
            self = self.right

        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        #start by applying the function to the root
        fn(self.value)

        #is there a left?
        if self.left:
            #then call the function again
            self.left.for_each(fn)
        #is there a right?
        if self.right:
            #then call the function again
            self.right.for_each(fn)

    def itertive_for_each(self, fn):
        stack = []

        #add the root node
        stack.append(self)

        #loop for as long as the stack has elements
        while len(stack) > 0:
            current = stack.pop()
            #take it out to perform function
            #then get any children to do the same
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)
            
    #Depth First traversal
    def breadth_first_for_each(self, fn):
        #this does the same thing as the function above
        #but it is moving laterally across the tree rather than
        #going down the list with recursion and applying
        #it to the children and then going up 

        #deque is a container similar to a list, appends/pops on both ends
        #but it is faster/more efficient than a rehular list
        #because python so smart
        queue = deque()

        #add the root node
        queue.append(self)

        #loop for as long as the stack has elements
        while len(queue) > 0:
            current = queue.popleft()
            #take out the furthest left value to apply the func to
            #both/any children are added to the right
            #this leads to nodes being handled in order, laterally
            if current.right:
                 queue.append(current.right)
            if current.left:
                 queue.append(current.left)

            fn(current.value)


    # Part 2 -----------------------

    # Lecture notes


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            #calling the left one first will make the recursion
            #go all the way down the left side, until it is at the smallest value
            #then it 'yoyos' back up, completing the unfinished nodes associated with the left
            #so if the smallest value was one, then node.left would be completed,
            #then the next value printed would be the node.value
            #then node.right is called, so that its left values can be printed
            #before printing the true right value
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        to_print = deque()

        #add the root node
        to_print.append(self)

        #loop for as long as the stack has elements
        while len(to_print) > 0:
            current = to_print.popleft()
            #take it out to perform function
            #then get any children to do the same
            #same exact logic as breadth first function application above
            if current.right:
                 to_print.append(current.right)
            if current.left:
                 to_print.append(current.left)

            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #initialize stack
        #push root to stack

        print(node.value)
        #just print the root and go down
        if node.right:
            node.right.dft_print(node.right)
        if node.left:
            node.left.dft_print(node.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

def half(x):
    return x / 2

print('Depth First Printing')
bst.dft_print(bst)

print('Breadth First Printing')
bst.bft_print(bst)

print('Pre-Order Depth First Printing')
bst.pre_order_dft(bst)

print('Post-Order Depth First Printing')
bst.post_order_dft(bst)