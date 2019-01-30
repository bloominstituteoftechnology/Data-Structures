class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = BinarySearchTree(value)
                    print(current.left.value)
                    break
                else:
                    current = current.left

            else:
                if current.right == None:
                    current.right = BinarySearchTree(value)
                    print(current.right.value)
                    break
                else:
                    current = current.right

    def contains(self, target):
        # if target > self.value:
        #   # search left side
        # elif target < self.value:
            # search right side

        current = self
        while True:
            if target == current.value:
                return True
            elif target < current.value: 
                if current.left is not None:
                    current = current.left
                    
                else:
                    return False
            elif target > current.value: 
                if current.right is not None:
                    current = current.right
                    
                else:
                    return False
            
        
        
        
        # while True:
        #   if current.value == target:
        #     return True
        #   elif target < current.value:
        #     current = current.left
        #   elif target < current.value:
        #     current = current.right
        #   else:
        #     if current.value == None:
        #       return False


    def get_max(self):
        # current = self
        # highestValue = 0
        # while True:
        #   if highestValue <
        pass





tree_test = BinarySearchTree(5)
tree_test.insert(2)
tree_test.insert(3)
tree_test.insert(7)
tree_test.insert(6)
print(tree_test.contains(8))
print(tree_test.right.value)
