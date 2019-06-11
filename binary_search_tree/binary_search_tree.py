class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self._max_level = None
        self._node = None


    @property
    def max_level(self):
        if self._max_level is None:
            if self.value is not None:
                self._max_level = self.get_max()
        return self._max_level

    @property
    def node(self):
        if self._node is None:
            if self.value is not None:
                self._node = BinarySearchTree(self.value)
        return self._node



    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)          



    def contains(self, value):
        if self.value == value:
            return True
        if self.left is not None:
            if value < self.value:
                return self.left.contains(value)
        if self.right is not None:
            if value > self.value:
                return self.right.contains(value)
        return False
        
    def get_max(self):
        smax = self.value
        lmax = None
        rmax = None
        if self.left != None:
            lmax = self.left.get_max()
        if self.right != None:
            rmax = self.right.get_max()
        a = [x for x in [smax,lmax,rmax] if x is not None]
        return max(*[a])
                    


    def get_max_level(self):

        if self.node is None: 
            return 0 
        else : 
            # Compute the height of each subtree  
            if self.node.left is not None:
                lheight = self.node.left.get_max_level()
            else:
                lheight = 0
            if self.node.right is not None:
                rheight = self.node.right.get_max_level()
            else:
                rheight = 0
    
            #Use the larger one 
            if lheight > rheight : 
                return lheight+1
            else: 
                return rheight+1   

    def contains(self, value):
        if self.value == value:
            return True
        if self.left is not None:
            if value < self.value:
                return self.left.contains(value)
        if self.right is not None:
            if value > self.value:
                return self.right.contains(value)
        return False

    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)                

