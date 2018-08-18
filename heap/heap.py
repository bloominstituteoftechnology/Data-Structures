from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = len(self.storage) - 1
 
  # def _left_child_value(i):
  #   if i > last_index:
  #     return None
  #   else:
  #     return self.storage[i*2]

  # def _right_child_value(i):
  #   if i > last_index:
  #     return None
  #   else:
  #     return self.storage[(i*2) + 1]

  # def _parent_value(i):
  #   if i == 0:
  #     return None
  #   else:
  #     return self.storage[i // 2]

  def insert(self, value):
    self.storage.append(value)
    
    
  def delete(self):
    pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
  
    current_value = self.storage[index]
    parent_value = current_value // 2

    while current_value != self.storage[1]:
      if parent_value <= current_value:
        parent_value, current_value = current_value, parent_value
      current_value = parent_value
    return current_value

  def _sift_down_(self):
    pass


my_heap = Heap()

my_heap.insert(42)
my_heap.insert(33)
my_heap.insert(100)
print(my_heap.storage)
