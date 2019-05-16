class Heap:
  def __init__(self):
    self.storage = []
    # for index i
    # to access the left child: 2i + 1
    # to access the right child: 2i + 2
    # to access the parent: (i - 1)//2

  def insert(self, value):
    self.storage.append(value)
    self.bubble_up(self.get_size() - 1)

  def delete(self):
    self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
    value_to_return = self.storage.pop()
    self._sift_down(0)
    return value_to_return

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def bubble_up(self, index):
		# in the worse case, the element will need to make it's way all 
		# the way to the top
      while index > 0:
        # get the parent element of this index
        # parent = math.floor((index-1) / 2)
        parent = (index - 1) // 2
        # Check if the element at index is higher priority than 
        # its parent element
        if self.storage[index] > self.storage[parent]:
          # If so, swap them
          # let's see it
          # :exploding_head:
          self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
          # What's missing? ....
          index = parent
        else: 
          # otherwise, our element is at a valid spot in the Heap
          # we no longer need to perform any more iterations of bubble_up
          break

  def _sift_down(self, index):
    # see if there is a left child node
    if (self.get_size() - 1) >= ((2 * index) + 1):
      # check if the left child node is bigger than the current node
      if self.storage[(2 * index) + 1] > self.storage[index]:
        
         # see if there is a right node
        if (self.get_size() - 1) >= ((2 * index) + 2):

          # check if the right node is bigger than the left node
          if self.storage[(2 * index) + 2] > self.storage[(2 * index) + 1]:
            # if the right is bigger than the left swap the right with the node at the current index
            self.storage[(2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
            # 
            self._sift_down((2 * index) + 2)
          else:
            # if it's bigger, swap it
            self.storage[(2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
            # now that you've swapped, check if we need to sift again
            self._sift_down((2 * index) + 1)
        else:
          # if it's bigger, swap it
          self.storage[(2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
          # now that you've swapped, check if we need to sift again
          self._sift_down((2 * index) + 1)
      else:
        # see if there is a right node
        if (self.get_size() - 1) >= ((2 * index) + 2):
          # print(f'{self.get_size()} - {(2 * index + 2)}')
          # check if the right child node is bigger than the current node
          if self.storage[(2 * index) + 2] > self.storage[index]:
            # if it's bigger, swap it
            self.storage[(2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
            # now that you've swapped, check if we need to sift again
            self._sift_down((2 * index) + 2)
          else:
            # there is a right child node but it is not bigger than
            # the current node (and we've already checked the left node)
            return
        # there is not a right child node (and not a left node)
        else:
          return
    else:
      # there is not a left or right child node
      pass