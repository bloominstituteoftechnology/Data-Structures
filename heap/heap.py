import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)
    
    
  def delete(self):
    self.storage[1], self.storage[-1] = self.storage[-1], self.storage[1]
    deleted_value = self.storage.pop(-1)
    self.size -= 1
    self._sift_down_(1)
    return deleted_value

  def get_max(self):
    return self.storage[1]

  def get_min(self):
    return self.storage[-1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
      # my two part base case for recursion: 
      # if parent is greater than child or if index less than or equal to one
      if self.storage[index] < self.storage[index//2] or index <= 1:
          return
      else:
          # swap the parent/child values
          self.storage[index], self.storage[index//2] = self.storage[index//2], self.storage[index]
          # recursive call
          return self._bubble_up(index//2)


  def _sift_down_(self, index):
    left_child = index * 2
    right_child = (index * 2) + 1
    if left_child > self.size:
      return
    if right_child <= self.size:
        if self.storage[index] < self.storage[left_child] or self.storage[index] < self.storage[right_child]:
            largest_child = right_child if (self.storage[right_child] > self.storage[left_child]) else left_child
            self.storage[index], self.storage[largest_child] = self.storage[largest_child], self.storage[index]
            return self._sift_down_(largest_child)
        else:
          return              
    else:
      if self.storage[index] < self.storage[left_child]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        return self._sift_down_(left_child)
      else:
        return
      
    

# heap = Heap()

# heap.insert(20)
# heap.insert(13)
# heap.insert(9)
# heap.insert(8)
# heap.insert(5)
# heap.insert(3)
# heap.insert(7)
# heap.insert(6)
# heap.insert(2)
# heap.insert(1)



# print(heap.storage)

heap2 = Heap()

heap2.insert(40)
heap2.insert(18)
heap2.insert(20)
heap2.insert(15)
heap2.insert(13)
heap2.insert(9)
heap2.insert(19)
heap2.insert(1)
heap2.insert(3)
heap2.insert(8)

print(heap2.storage)

heap2.delete()
print("heap2 after delete(): ", heap2.storage)

heap2.insert(40)
print("After 40 resinserted: ", heap2.storage)
