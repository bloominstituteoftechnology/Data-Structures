class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        #If the value is > then root:
        if value > self.value:

            # If there's no value on the right set it to a new BST(value)
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:

                #This right here is magic! Call insert on self.right,
                #which is just a BST also!!! FAAAK!
                self.right.insert(value)

        else:

            # If there's no value on the left set it to a new BST(value)
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


    def contains(self, target):
        #First check the root node:
        if self.value == target:
            return True

        #Check if either the left or right node are leafs 
        elif self.left == None or self.right == None:
            return False
        
        #Since they are not leafs, they have values...
        else:
            if target > self.value :
                return self.right.contains(target)
            else:
                return self.left.contains(target)

    def get_max(self):
        # Recursive
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


        #Interative:
        # curr = self
            
        # if curr:
        #     curr = curr.right

        # return curr.value