class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self is not None and value is not None:
            if value < self.value:
                self.left = self.__init__(value)
            else:
                self.right = self.__init__(value)
        
    def contains(self, target):
        '''
        while self.value is None:  
            if self is not None and target is not None:
                pointer = self
                if target < pointer.value:
                    pointer = self.left
                elif target > pointer.value:
                    pointer = self.right
                else:
                    return True
        return False
        '''
        pass
    def get_max(self):
        '''
        while self.value != None:  
            if self is not None:
                pointer = self
                if pointer.value < self.right.value:
                    pointer = self.right
                else:
                    return pointer.value
        return None
        '''
        pass