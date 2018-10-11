class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

   
      # print('\nnew inner')
      # print(new_value, parent.value)
      if value < self.value:
        if self.left == None: 
          # print('-left if return -')
          self.left = BinarySearchTree(value)
          # return self.left.value
          #maybe don't need
        else: 
          # print('left else')
          # self.left = BinarySearchTree(self.left)
          # print(new_value, self.left)
          return self.left.insert(value)
          #self.left.insert 
          # print('else')   
      elif value > self.value:
        # print('new_value > parent')
        # print(self.right, 'right')
        if self.right == None:
          # print('-right if return-')
          self.right = BinarySearchTree(value)
          # return self.right.value
        else: 
          # print('right else')
          # self.right = BinarySearchTree(self.right)
          # print(new_value, self.right)
          return self.right.insert( value)
          # print('else')
          #go down a level 
      else: 
        print('not a number?')

    # print(self.value, 'value')
    # print(self.right, 'right')
    # print(self.left, 'left')
    # print(value, 'new_value')



  def contains(self, target):
    pass

  def get_max(self):
    pass

# old and bad code
# def insert(self, value):

#     def inner(new, parent):
#       print('\nnew inner')
#       print(new_value, parent.value)
#       if new_value < parent.value:
#         if self.left == None: 
#           print('-left if return -')
#           self.left = BinarySearchTree(new_value)
#           return self.left.value
#         else: 
#           print('left else')
#           # self.left = BinarySearchTree(self.left)
#           print(new_value, self.left)
#           return inner(new_value, self.left)
#           #self.left.insert 
#           # print('else')   
#       elif new_value > parent.value:
#         print('new_value > parent')
#         print(self.right, 'right')
#         if self.right == None:
#           print('-right if return-')
#           self.right = BinarySearchTree(new_value)
#           return self.right.value
#         else: 
#           print('right else')
#           self.right = BinarySearchTree(self.right)
#           print(new_value, self.right)
#           return inner(new_value, self.right)
#           # print('else')
#           #go down a level 
#       else: 
#         print('not a number?')

#     # print(self.value, 'value')
#     # print(self.right, 'right')
#     # print(self.left, 'left')
#     # print(value, 'new_value')
#     new_value = value 
#     parent_value = self

#     return inner(new_value, parent_value)