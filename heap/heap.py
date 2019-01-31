class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.size += 1
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    self.size -= 1
    deleted_node = self.storage[0]
    del(self.storage[0])
    return deleted_node

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
          self.storage[index], self.storage[(
              index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2
 

  def _sift_down(self, index):

    left = index * 2
    right = index * 2 + 1
    largest = index

    if len(self.storage) > left and self.storage[largest] < self.storage[left]:
      largest = left
      
    if len(self.storage) > right and self.storage[largest] < self.storage[right]:
      largest = right
    
    if largest != index:
      self._swap(index, largest)
      self._sift_down(largest)
   

  def _swap(self, i, j):
    self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
    
    


def heapsort(arr):
    newArr = []
    newHeap = Heap()

    for item in arr:
        newHeap.insert(item)

    for x in range(newHeap.get_size()):
        j = newHeap.delete()
        newArr.insert(0, j)

    print(newArr)
    return newArr

heapsort([1,2,4,5,6,2,3,4,5,])
# new_heap.insert(10)
# new_heap.insert(2)
# print(new_heap.storage)
# # print(new_heap.delete())
# # print(new_heap.delete())
# # print(new_heap.delete())
# print(new_heap.storage)

# print(new_heap.get_max())
# print(new_heap.get_size())
# print(new_heap.storage)