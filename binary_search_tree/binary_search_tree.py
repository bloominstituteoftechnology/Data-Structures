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
        self.left  = None
        self.right = None
        self.count = 1

    # Insert the given value into the tree
    def insert(self, value):
        # Is the value less than the current node's value?
        if value < self.value:
            # insert to the left
            if self.left == None:
                # No "left" child, insert the new node here
                self.left = BSTNode(value)
            else:
                # a "left" child exists, invoke the the child's insert method
                self.left.insert(value)
        
        # Is the value equal to the current node's value?
        if value == self.value:
            # Does the current node have a "right" child
            if self.right == None:
                # No "right" child -> add this value as the current node's 
                #   right child
                self.right = BSTNode(value)
            else:
                # A current right child exists
                tmp_node        = BSTNode(value)    # Create a node
                tmp_node.right  = self.right        # Make the existing right node a child 
                                                    #    of the new node
                self.right      = tmp_node          # Make the new node the "right" child 
                                                    #    of current node

        # Is the value greater than the current node's value?
        if value > self.value:
            # insert to the right
            if self.right == None:
                # No "right" child, insert the new node here
                self.right = BSTNode(value)
            else: 
                # a "right" child exists, invoke the the child's insert method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Is this the target node?
        if self.value == target:
            return True

        # Not the target node, is the target less than the current node?
        if target < self.value:
            # Are there any "left" nodes to search?
            if self.left == None:
                # No more nodes to search -> the target is not found
                return False

            # A left node or sub-tree exists, return an invocation
            #   of the contains method on the left child node
            return self.left.contains(target)

        # Not the target node, is the target greater than the current node?
        if target > self.value:
            # Are there any "right" nodes to search?
            if self.right == None:
                # No more nodes to search -> the target is not found
                return False

            # A right node or sub-tree exists, return an invocation
            #   of the contains method on the right child node
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Does the node have a "right" child
        #  (if so, that node value is greater than the current node)
        if self.right == None:
            # No right child, this node's value is the max value
            return self.value

        # A right node exists, return an invocation of the 
        #   get_max method on the right child node
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call the function on this node's value
        fn(self.value)

        # Does this node have a "left" child?
        if self.left != None:
            # A left child exists; invoke the for_each method on that child
            self.left.for_each(fn)

        # Does this node have a "right" child?
        if self.right != None:
            # A left child exists; invoke the for_each method on that child
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, target=None):
        if target == None:
            target = self

        # Does this node have a "left" child?
        if target.left != None:
            # A "left" child exists, invoke the in_order_print on
            #    the left child
            target.left.in_order_print()

        # Exhausted the left children, now print this node
        print(target.value)

        # Does this node have a "right" child?
        if target.right != None:
            # A "right" child exists, invoke the in_order_print on
            #    the right child
            target.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, target=None):
        if target == None:
            target = self
        
        map_lvl = {}        # Create a map to keep track of nodes by tree "level"
        ctnu    = True      # Flag that drives processing    
        lvl     = 1         # Current tree level being processed

        # Assume this node is the root of our tree (or sub-tree)
        map_lvl[lvl] = [target]

        # Iterate across and down the tree while the ctnu flag is true
        while ctnu:
            lvl = lvl + 1               # Iterate on the next level
            map_lvl[lvl] = []           # Initialize a node list for this level
            ctnu = False                # Assume we're done after this iteration (unless noted)
            
            # Inspect the nodes of the last level (do they have children?)
            for nde in map_lvl[lvl-1]:
                # Do we have a "left" child?
                if nde.left != None:
                    map_lvl[lvl].append(nde.left)   # Yes, found a "left" child
                    ctnu = True                     # Inspect another level after this

                if nde.right != None:               
                    map_lvl[lvl].append(nde.right)  # Yes, found a "right" child
                    ctnu = True                     # Inspect another level after this

        # Print out the nodes
        keys_lst = list(map_lvl.keys())
        keys_lst.sort()

        # Iterate through the levels of the tree
        for key in keys_lst:
            for nd in map_lvl[key]:
                # Do we have a node? If yes, print
                if nd != None:
                    print(nd.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print_old(self, target=None):
        if target == None:
            target = self
        
        map_lvl = {}        # Create a map to keep track of nodes by tree "level"
        ctnu    = True      # Flag that drives processing    
        lvl     = 1         # Current tree level being processed

        # Assume this node is the root of our tree (or sub-tree)
        map_lvl[lvl] = [target]

        # Iterate across and down the tree while the ctnu flag is true
        while ctnu:
            lvl = lvl + 1               # Iterate on the next level
            map_lvl[lvl] = []           # Initialize a node list for this level
            ctnu = False                # Assume we're done after this iteration (unless noted)
            
            # Inspect the nodes of the last level (do they have children?)
            for nde in map_lvl[lvl-1]:
                # Do we have a "left" child?
                if nde.left != None:
                    map_lvl[lvl].append(nde.left)   # Yes, found a "left" child
                    ctnu = True                     # Inspect another level after this

                if nde.right != None:               
                    map_lvl[lvl].append(nde.right)  # Yes, found a "right" child
                    ctnu = True                     # Inspect another level after this

        # Sort the tree levels in numeric order (1, 2, 3,...)
        keys_lst = list(map_lvl.keys())
        keys_lst.sort()

        # Determine the max number of nodes across all levels
        max_num_nodes = 1
        for lv in keys_lst:
            if len(map_lvl[lv]) > max_num_nodes:
                # This level has more nodes than our previous max
                #   set new max number of nodes
                max_num_nodes = len(map_lvl[lv])

        # Pad each level array (list) with None so that
        #   each level array has max_num_nodes elements
        for lv in keys_lst:
            pad_num = max_num_nodes - len(map_lvl[lv])
            if pad_num > 0:
                for n in range(pad_num):
                    map_lvl[lv].append(None)

        # Iterate through each vertical slice of the tree
        for slc in range(max_num_nodes):
            # Iterate through each level of the tree
            for lv in keys_lst:
                # Print each element if not equal to None
                if map_lvl[lv][slc] != None:
                    print(map_lvl[lv][slc].value)

    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, target=None):
        if target == None:
            target = self
        
        wrk_stack = []

        # Add the passed node to the stack
        wrk_stack.append(target)

        # Is the stack empty
        while len(wrk_stack) != 0:
            tmp_node = wrk_stack.pop(0) # pop the first node from the stack
            print(tmp_node.value)       # print out the node value
            
            # place the right child on the stack (if it exists)
            if tmp_node.right != None:
                wrk_stack.insert(0, tmp_node.right)

            # place the left child on the stack (if it exists)
            if tmp_node.left != None:
                wrk_stack.insert(0, tmp_node.left)
    
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

 
