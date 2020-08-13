    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case: check self's value to see if it matches the target's 
        if self.value == target:
            return True
        # otherwise, we need to go either left or right 
        # compare the target against self's value 
        if target < self.value:
            # base case: if there's no node here, then the target is not in the tree
            if not self.left:
                return False
            # otherwise, there is a node there
            else:
                # call `contains` on the left child
               return self.left.contains(target) 
        else:
            # base case: if there's no node here, then the target is not in the tree
            if not self.right:
                return False
            # otherwise there's a node there 
            else:
                # call `contains` on the right child 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # the max value is always going to be the right-most tree node 
        # Recursive version 
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # Iterative version 
        current = self

        while current.right:
            current = current.right

        # `current` doesn't havea right 
        return current.value

    # Call the function `fn` on the value of each node
    # This method doesn't return anything 
    def for_each(self, fn):
        # Recursive 
        # call fn on self.value 
        # fn(self.value)
        # # check if self has a left child 
        # if self.left:
        #     # call `for_each` on the left child, passing in the fn 
        #     self.left.for_each(fn)
        # # check if self has a right child 
        # if self.right:
        #     # call `for_each` on the right child, passing in the fn 
        #     self.right.for_each(fn)

        # # Depth-First Iterative 
        # # how do we achieve the same ordering that recursion gave us for free? 
        # # use a stack to achieve the same ordering 
        # stack = [] 
        # # add the root node to our stack 
        # stack.append(self)

        # # continue popping from our stack so long as there are nodes in it 
        # while len(stack) > 0:
        #     current_node = stack.pop()

        #     # check if this node has children 
        #     if current_node.right:
        #         stack.append(current_node.right)
        #     if current_node.left:
        #         stack.append(current_node.left)
            
        #     fn(current_node.value)

        # Breadth-First traversal 
        from collections import deque

        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()

            # check if this node has children 
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.righ)

            fn(current_node.value)