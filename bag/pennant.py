import math

"""
A Pennant is comprised of a unary root whose
child is a complete Binary Tree. Each Pennant
node stores a value. Bags store multiple 
Pennants in order to store any arbitrary
number of elements.
"""
class Pennant:
    """
    A Pennant's constructor consists of the value it's 
    holding, the total count of nodes in the Pennant,
    a left and right child OR a single child in `middle`.
    k is the log of `count` in base 2. 
    """
    def __init__(self, value=None):
        self.value = value
        self.count = 1
        self.middle = None
        self.left = None
        self.right = None
        self.k = 0
        
    def combine(self, pennant):
        """
        Method to combine two Pennants into a 
        new Pennant whose total number of nodes
        is 2^(k+1) where k is the k value of the 
        prior Pennant. Note that the Bag will 
        maintain the invariant that only Pennants
        of equal k value will be combined together.
        """
        # Root of the pennant has no `middle` child
        # Thus this pennant has no children
        if not self.middle:
            self.middle = pennant
            self.count += 1
            self.k = 1
        else:
            x = self.middle
            y = pennant.middle
            self.middle = pennant
            pennant.left = x
            pennant.right = y
            pennant.middle = None
            self.count += pennant.count
            self.k = math.log2(self.count)

    def split(self):
        """
        Method to perform the inverse of the combine
        method. Splits a Pennant into two Pennants of
        equal size, updating each new Pennant's k
        value accordingly. 
        """
        if self.middle:
            new_pennant = self.middle
            self.middle = new_pennant.left
            new_pennant.middle = new_pennant.right
            new_pennant.left = None
            new_pennant.right = None

            self.count = self.count // 2
            self.k = math.log2(self.count)

            new_pennant.count = self.count
            new_pennant.k = self.k

            return new_pennant


    
