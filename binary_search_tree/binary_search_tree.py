"""
I want to check if a root has been set. If there is no root then I should be able to set the value to the root.   from there  I want to   check all new values 
if  the new value is less than the root we then move left if it is greater move right.   

to me looking at this some recursion maybe neccessary.   because not only is there a check for if there is a right but we are also checking for if there is another item 

so   8 == root       6 comes along     check if 8 already has a child to the left  if it doesn't set it.    if it does  now we need to compare that item to make the decision to 
go left or right.   This would be repeated until the newest item becomes a leaf meaning it has no children.  

I have some functions to use for this maybe too many.   But defintely enough     returning True or false   and moving accordingly.   

Off hand I want to do something like   self.root == None   then   create a TreeNode and set it to root. 
"""


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None, root=None):
        self.key = key or value 
        self.left = left
        self.right = right
        self.parent = parent
        self.root = root
    # End of Initializing

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isLeft(self):
        return self.parent and self.parent.left == self

    def isRight(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def has_a_child(self):
        return self.right or self.left

    def has_max_children(self):
        return self.right and self.left

    def __iter__(self):  # if it is desired to iterate over the entire tree.
        if self:
            if self.hasLeft():
                for elem in self.left:
                    # this will pause and allow to use the next() function to  go back to where we left off in the code.
                    yield elem
            yield self.key
            if self.hasRight():
                for elem in self.rightChild:
                    # this will pause and allow to use the next() function to  go back to where we left off in the code.
                    yield elem

    def replaceNodeData(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = lc
        self.right = right
        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self

# def _setitem__(self, k,v):
#     self.put(k,v)

# def _getitem__(self,key):
#     return self.get(key)

# def __contains__(self,key):
#     if self.__contains(key,self.root):
#         return True
#     else:
#         return False


#

class BinarySearchTree:
    def __init__(self, value):
        self.root = None
        self.size = 0

    def insert(self, value):
        # need to check if there is a root, if there isn't set the first item as the root.
        if self.root:
            self.__insert( value, self.root)
        else:
            self.root = TreeNode(value)
        self.size += 1

    def __insert(self, key, currentNode):
        # this is a helper function
        # This is where we are checking to see if we are going to go left or right. If this is true we go left.
        if key < currentNode.key:

            if currentNode.hasLeft():  # Returns True or False depending on if there is a left Child already
                # ^The line above is also the base case  the recursive lines are working to get to this line where it wil come back false.
                # This is recursion because there is a left already we know need to check if we need to go left or right of it.
                self._insert(key, currentNode.left)
            else:  # There is no left for the current node and we are headed left.
                # Creation of a new TreeNode because we have reached a leafy area.
                currentNode.left = TreeNode(key, parent=currentNode)
        else:  # key is greater than currentNode.key so we will head to the right of it.
            if currentNode.hasRight():  # returns True or False depending on if there is a right Child already
              # ^The line above is also the base case  the recursive lines are working to get to this line where it wil come back false.
                # This is recursion because there is a left already we know need to check if we need to go left or right of it.
                self.__insert(key, currentNode.right)
            else:  # there is no right and we are headed right.
                # Creation of a new TreeNode because we have reached a leafy area.
                currentNode.right = TreeNode(key, parent=currentNode)
        # Each time we add a new node we should reach a leafy area meaning a area where the node has no children.
        # It may at a time become a parent but for now it is just a child.

    def contains(self, target):
        """ 
        So a check for has_max_children should go first. At this point if True there is a left and a right. 
        Now  if the item is actually a number   then finding the target becomes easy.  I guess it depends on how its all set up. 
        If its set up in alphabetical order  where  "a"  < "b"   == True  then we can find the target easily  by going left for less, 
        right for greater.   if its not sorted   then    has_max_children would be needed a check on both sides needs to be done. 
        Not sure if all data will be sorted but  there is the opprotunity to at least implement some kind of sorting myself on the insert. 

        """
        if self.root:  # Checking to make sure there is a
            result = self.__contains(target, self.root)
            if result:
                return result.value
            else:
                return None
        else:
            # if no root is set we have no searching to do there is nothing in the tree.
            return None

    def __contains(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:  # found it!
            return currentNode  # this is what we are working towards finding the target
        elif key < currentNode.key:
            # recursion we are working towards line 118 or 120
            return self.__contains(key, currentNode.left)
            # 120 if target is in the in the tree and 118 if the traget is not in the tree
        else:
            # recursion we are working towards line 118 or 120
            return self.__contains(key, currentNode.right)
            # 120 if target is in the in the tree and 118 if the traget is not in the tree

    def get_max(self):
        """No input Output will be the max  either a value or None if tree is empty.  """
        current = self
        while current.hasRight():  # This is the belief that the max has to be to the right. If you can't go right either in the begining or any more
            # if current has a right this line will be set  and will keep going from line 129 to 130 until there are no more rights.
            current = current.right
        # this line returns   as soon there is no more rights.  breaking out of the loop.
        return current

    def __iter__(self):
        # allows you to iterate through the binary search tree.
        return self.root.__iter__()
