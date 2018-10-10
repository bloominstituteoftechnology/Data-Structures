from math import floor

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    pass

  def get_max(self):
    print('current state of storage:',self.storage)
    return self.storage[1]

  def get_size(self):
    pass

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
    pass

def main():
  my_heap = Heap()
  my_heap.insert(6)
  my_heap.insert(8)
  my_heap.insert(10)
  my_heap.insert(9)
  my_heap.insert(1)
  my_heap.insert(9)
  my_heap.insert(9)
  my_heap.insert(5)
  my_heap.insert(69)
  print('get_max result:',my_heap.get_max())

if __name__ == '__main__':
  main()

"""
**Bubble Up**
* `node = i` (`i` must != `0`)
* `left = 2i`
* `right = 2i + 1`

**Child to Parent**
`floor(i/2)`
"""