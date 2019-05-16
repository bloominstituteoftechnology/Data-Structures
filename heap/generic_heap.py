
# To access the left child: 2i + 1
# To access the right child: 2i + 2
# To access the parent: (i - 1) // 2

class Heap:
  def _init_(self):
    self.storage = []
    
  def insert(self, value):
    pass
  
  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

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
		


  def _sift_down(self, index):
    pass		