"""
I want to check if a root has been set. If there is no root then I should be able to set the value to the root.   from there  I want to   check all new values 
if  the new value is less than the root we then move left if it is greater move right.   

to me looking at this some recursion maybe neccessary.   because not only is there a check for if there is a right but we are also checking for if there is another item 

so   8 == root       6 comes along     check if 8 already has a child to the left  if it doesn't set it.    if it does  now we need to compare that item to make the decision to 
go left or right.   This would be repeated until the newest item becomes a leaf meaning it has no children.  

I have some functions to use for this maybe too many.   But defintely enough     returning True or false   and moving accordingly.   

Off hand I want to do something like   self.root == None   then   create a TreeNode and set it to root. 
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.size = 0
        self.left = None
        self.right = None 

    def insert(self, value):
        current = self
        self.size += 1
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = BinarySearchTree(value)
                    #here is the base case we are working towards
                    #finding a None. 
                    break
                else:
                    current = current.left
                    #^This line is kind of similar to recursion
                    # keep going until the base case is reached.
            else:
                if current.right ==None:
                    current.right = BinarySearchTree(value)
                    #here is the base case we are working towards
                    #finding a None. 
                    break
                else:
                    current = current.right 
                    #^This line is kind of similar to recursion
                    # keep going until the base case is reached.

    #"""There is no need for  the Tree Node as well this won't pass the Lambda test """
    # def __insert(self, key, currentNode):
    #     # this is a helper function
    #     # This is where we are checking to see if we are going to go left or right. If this is true we go left.
    #     if key < currentNode.key:

    #         if currentNode.hasLeft():  # Returns True or False depending on if there is a left Child already
    #             # ^The line above is also the base case  the recursive lines are working to get to this line where it wil come back false.
    #             # This is recursion because there is a left already we know need to check if we need to go left or right of it.
    #             self._insert(key, currentNode.left)
    #         else:  # There is no left for the current node and we are headed left.
    #             # Creation of a new TreeNode because we have reached a leafy area.
    #             currentNode.left = TreeNode(key, parent=currentNode)
    #     else:  # key is greater than currentNode.key so we will head to the right of it.
    #         if currentNode.hasRight():  # returns True or False depending on if there is a right Child already
    #           # ^The line above is also the base case  the recursive lines are working to get to this line where it wil come back false.
    #             # This is recursion because there is a left already we know need to check if we need to go left or right of it.
    #             self.__insert(key, currentNode.right)
    #         else:  # there is no right and we are headed right.
    #             # Creation of a new TreeNode because we have reached a leafy area.
    #             currentNode.right = TreeNode(key, parent=currentNode)
    #     # Each time we add a new node we should reach a leafy area meaning a area where the node has no children.
    #     # It may at a time become a parent but for now it is just a child.
    #     if self.head is None and self.tail is None:
    #         self.head = currentNode
    #         self.tail = currentNode 
    #     else:
    #         self.tail = currentNode


    def contains(self, target):
        """ 
        So a check for has_max_children should go first. At this point if True there is a left and a right. 
        Now  if the item is actually a number   then finding the target becomes easy.  I guess it depends on how its all set up. 
        If its set up in alphabetical order  where  "a"  < "b"   == True  then we can find the target easily  by going left for less, 
        right for greater.   if its not sorted   then    has_max_children would be needed a check on both sides needs to be done. 
        Not sure if all data will be sorted but  there is the opprotunity to at least implement some kind of sorting myself on the insert. 

        """
        current = self 
        while True:
            if current.value == target:
                return True # Here is base case we are working towards. 
            elif target < current.value:
                if current.left is not None:
                    current = current.left # this line is our recursive or could be recursive in the while that is working towards base case. 
                else:
                    return False # it doesn't exist if we have reached a leaf which is the only way we can reach None. 
            elif target > current.value:
                if current.right is not None:
                    current = current.right  #this line is our recursive or could be recursive in the while that is working towards base case.
                else:
                    return False # it doesn't exist if we have reached a leaf which is the only way we can reach None. 

    def get_max(self):
        """No input Output will be the max  either a value or None if tree is empty.  """
        current = self
        while current.hasRight():  # This is the belief that the max has to be to the right. If you can't go right either in the begining or any more
            # if current has a right this line will be set  and will keep going from line 129 to 130 until there are no more rights.
            current = current.right
        # this line returns   as soon there is no more rights.  breaking out of the loop.
        return current.value

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right
