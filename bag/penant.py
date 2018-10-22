import math

class Penant:
    def __init__(self, value=None):
        self.value = value
        self.count = 1
        self.middle = None
        self.left = None
        self.right = None
        self.k = 0

    def determine_k(self):
        return math.log2(self.count)
        
    def combine(self, penant):
        # combining two one-element penants
        if not self.middle:
            self.middle = penant
            self.count += 1
            self.k = 1
        else:
            x = self.middle
            y = penant.middle
            self.middle = penant
            penant.left = x
            penant.right = y
            penant.middle = None
            self.count += penant.count
            self.k = self.determine_k()


    def split(self):
        if self.middle:
            new_penant = self.middle
            self.middle = new_penant.left
            new_penant.middle = new_penant.right
            new_penant.left = None
            new_penant.right = None

            self.count = self.count // 2
            self.k = self.determine_k()

            new_penant.count = self.count
            new_penant.k = self.k

            return new_penant


    