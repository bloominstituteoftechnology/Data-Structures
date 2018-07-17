class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
            
    def insert(self, value):
        val = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = val
                #attaching a new node here
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = val
            else:
                self.right.insert(value)
        
    def contains(self, target):
        pointer = self
        while pointer:
            if target == pointer.value:
                print("nacho bc")
                return True
            elif target < pointer.value:
                pointer = pointer.left
            else:
                pointer = pointer.right

        return False
        
    def get_max(self):
        pointer = self
        while pointer.right: 
            print("xoo")
            print(self.value)
            pointer = pointer.right
        
        return pointer.value