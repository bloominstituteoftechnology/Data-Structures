class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None, root=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.root = root
    #End of Initializing 
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


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # need to check if there is a root, if there isn't set the first item as the root.
        if self.root == None:
            pass

    def contains(self, target):
        """ 
        So a check for has_max_children should go first. At this point if True there is a left and a right. 
        Now  if the item is actually a number   then finding the target becomes easy.  I guess it depends on how its all set up. 
        If its set up in alphabetical order  where  "a"  < "b"   == True  then we can find the target easily  by going left for less, 
        right for greater.   if its not sorted   then    has_max_children would be needed a check on both sides needs to be done. 
        Not sure if all data will be sorted but  there is the opprotunity to at least implement some kind of sorting myself on the insert. 

        """
        pass

    def get_max(self):
        current = self
        while current.hasRight():
            current = current.right
        return current

    
       
