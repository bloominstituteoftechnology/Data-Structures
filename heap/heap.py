class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
      length = len(self.storage)
      self.size += 1
      
      if length == 1 or value > self.storage[1]:
          self.storage.insert(1, value)
          return
      else:
          self.storage.append(value)

  def delete(self):
      if len(self.storage) == 1:
          return None
      
      max_value = self.storage[1]
      new_max = 0
      new_max_index = 0

      self.storage.remove(self.storage[1])

      for i in range(1, len(self.storage)):
          if self.storage[i] > new_max:
              new_max = self.storage[i]
              new_max_index = i

      self.storage.remove(self.storage[ new_max_index ])
      self.storage.insert(1, new_max)

      self.size -= 1
      return max_value

  def get_max(self):
      return self.storage[1]

  def get_size(self):
      return self.size

  def _bubble_up(self, index):
      """
      How to find the left and right children of a parent node if your binary tree starts at array index 1 instead of 0
      left = 2 * index
      right = 2 * index + 1

      How to find a left child nodes parent node index if binary tree starts at 1 instead of 0
      parent = index / 2

      How to find a right child nodes parent node index if binary tree starts at 1 instead of 0
      parent = (index - 1) / 2
      """
      if not self.storage[ index ]:
          return False

      if index % 2 == 0:
          parent_node = self.storage[ index // 2 ]

          if self.storage[ index ] > parent_node:
              temp = self.storage[ index ]
              self.storage[ index ] = parent_node
              self.storage[ index // 2 ] = temp
      else:
          parent_node = self.storage[ (index - 1) // 2 ]

          if self.storage[ index ] > parent_node:
              temp = self.storage[ index ]
              self.storage[ index ] = parent_node
              self.storage[ (index - 1) // 2 ] = temp

  def _sift_down(self, index):
      left_child_index = index * 2
      right_child_index = index * 2 + 1
      left_child = None
      right_child = None
      largest_child = None
      
      if len(self.storage) > left_child_index:
        left_child = self.storage[ left_child_index ]

      if len(self.storage) > right_child_index:
        right_child = self.storage[ right_child_index ]

      if left_child:
          if right_child:
            if left_child > right_child:
                largest_child = left_child
            else:
                largest_child = right_child
            