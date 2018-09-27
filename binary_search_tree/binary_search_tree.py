##### Attempt 2 (off-the-top) #######
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass



bst1 = BinarySearchTree(5)
print(bst1.value)






###### Attempt 1 (Correct) #######
# class BinarySearchTree:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None

#   def insert(self, value):
#     if self.value:
#       if value < self.value:
#         if self.left is None:
#           self.left = BinarySearchTree(value)
#         else:
#           self.left.insert(value)
#       elif value > self.value:
#         if self.right is None:
#           self.right = BinarySearchTree(value)
#         else:
#           self.right.insert(value)
#     else:
#        self.value = value

#   def contains(self, target):
#     if target == self.value:
#       return True
#     elif target < self.value and self.left:
#       return self.left.contains(target)
#     elif target > self.value and self.right:
#       return self.right.contains(target)
#     return False

#   def get_max(self):
#     if self.value:
#       if self.right is None:
#         return self.value
#       else:
#         return self.right.get_max()
#     else:
#       return False



# root = BinarySearchTree(5)


# root.insert(10)
# # root.insert(4)
# # root.insert(3)
# # root.insert(39)
# # root.insert(30)
# # root.insert(60)
# # root.insert(47)

# print(root.contains(47))
# print(root.get_max())