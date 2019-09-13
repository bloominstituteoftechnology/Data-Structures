import math
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        #Create a new node here with value is value in node
        new_node = BinarySearchTree(value)
        root = self #This is the root of binary tree
        while True:
            if root.value > new_node.value:
                if root.left == None:
                    root.left =new_node
                    return
                else:
                    root = root.left
            else:
                if root.right==None:
                    root.right=new_node
                    return
                else:
                    root = root.right
        #Start looking where this new node with value will go



    def contains(self, target):
        root=self
        while True:
            if root.value ==target:
                return True

            if root.value>target:
                if root.left==None:
                    return False
                else:
                    root=root.left

            else:
                pass
                if root.right == None:
                    return False
                else:
                    root = root.right

    def get_max(self):
        root=self


        while root:
            if root.right == None:
                return root.value
            root = root.right

    def for_each(self, cb):
        # preorder
        root=self

        if self.left:
           self.left.for_each(cb)
        cb(self.value )
        if self.right:
           self.right.for_each(cb)
