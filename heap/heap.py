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
    if self.size < 1:
      return None
    elif self.size == 1:
      self.size -= 1
      return self.storage.pop()
    else:
      # print('delete prev state:',self.storage)
      # print(self.storage[2:])
      # print([0] + self.storage[2:])
      temp = self.storage[self.size]
      
      self.storage[self.size] = self.storage[1]
      self.storage[1] = temp
      
      deleted_item = self.storage.pop()
      print(self.storage)
      # self.storage = [0] + self.storage[2:]
      # print('delete inter state:',self.storage)
      # self.storage.insert(1, self.storage.pop())
      # print('delete after state:',self.storage)
      self.size -= 1
      self._sift_down(1)
      return deleted_item


  def get_max(self):
    print('current state of storage:',self.storage)
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # Definitions
    sub_index = floor(index/2)
    num_considered = self.storage[index]
    parent = self.storage[sub_index]

    # Base Case
    if index == 1: return

    # Swap
    if num_considered > parent:
      self.storage[sub_index] = num_considered
      self.storage[index] = parent
    else: return # Stop because number is in the right place

    # Do it again
    self._bubble_up(sub_index)
      

  def _sift_down(self, index):
    # Definitions
    num_considered = self.storage[index]
    left_i = 2 * index
    right_i = 2 * index + 1
    print("_sift_down beginning:",self.storage,'self.size:',self.size)
    # print('_sift_down prev state:',self.storage)
    if left_i > self.size and right_i > self.size:
      return
    
    if right_i > self.size:#3 > 2
      temp = self.storage[left_i]
      self.storage[left_i] = num_considered
      self.storage[index] = temp
      self._sift_down(left_i)
      return

    # Base Case
    # if index == len(self.storage) - 1: return
    
    # Swap
    left_num = self.storage[left_i]
    right_num = self.storage[right_i]
    if right_num <= left_num:
      self.storage[left_i] = num_considered
      self.storage[index] = left_num
      self._sift_down(left_i)
    else:
      self.storage[right_i] = num_considered
      self.storage[index] = right_num
      self._sift_down(right_i)
    # else:
      # print('_sift_down after state:',self.storage)
      # return
    
    # print('_sift_down after state:',self.storage)

def main():
  my_heap = Heap()
  my_heap.insert(6)
  my_heap.insert(8)
  my_heap.insert(10)
  my_heap.insert(9)
  my_heap.insert(1)
  my_heap.insert(5)
  print('get_max result:',my_heap.get_max())
  # my_heap.delete()
  # print('get_max result:',my_heap.get_max())
  # my_heap.delete()
  # print('get_max result:',my_heap.get_max())
  descending_order = []
  while my_heap.get_size() > 0:
    print("my_heap storage:",my_heap.storage)
    descending_order.append(my_heap.delete())
    print("descending order:",descending_order)

if __name__ == '__main__':
  main()

"""
**Parent to Child**
* `node = i` (`i` must != `0`)
* `left = 2i`
* `right = 2i + 1`

**Child to Parent**
`floor(i/2)`
"""