from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0


  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)
    
  def delete(self):
    pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
      current_index = index
      
      
      while current_index != 1:
        if self.storage[current_index] > self.storage[current_index // 2]:
          self.storage[current_index], self.storage[current_index // 2] = self.storage[current_index // 2], self.storage[current_index]
        current_index = current_index // 2
      return self.storage[current_index]

  def _sift_down_(self, index):
    pass


my_heap = Heap()
entries  = [20, 13, 9, 8, 5, 3, 7, 6, 2, 1]
for i in range(len(entries)):
  my_heap.insert(entries[i])
print(my_heap.storage)
heap = Heap()
more_entries = [6, 7, 5, 8, 10, 1, 2, 5]
for i in range(len(more_entries)):
  heap.insert(more_entries[i])
print(heap.storage)
