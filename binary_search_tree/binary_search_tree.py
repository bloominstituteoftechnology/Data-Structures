class BinarySearchTree:
      def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if self.value:
           if value < self.value:
  
            if self.left is None:
              self.left = Node(data)
          else:
              self.left.insert(value)
      elif data > self.value:
              if self.right is None:
                    self.right = Node(value)
              else:
                    self.right.insert(Value)
        else:
            self.value = value
  
                    
    

  def contains(self, target):
    pass

  def get_max(self):
    pass
