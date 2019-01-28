class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #check to see if there is a root
    if self.value == None:
      #assign value to root
      vale = self.value
    #check if root is greater or equal than value
    else:
      if self.value >= value:
        if self.right == None:
          self.value = value



    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass
