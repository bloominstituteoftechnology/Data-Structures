class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    index = self.count
    self.storage.append(value)
    self._bubble_up(index)
    self.count += 1

  def delete(self):
    if self.count > 0:
      retval = self.get_max()
      print(f'before delete: {self.storage}')# <-- debugging
      last = self.storage.pop()
      self.storage[0] = last
      self.count -= 1
      print(f'after delete: {self.storage}')# <-- debugging
      self._sift_down(0)
      print(f'after sift down: {self.storage}')# <-- debugging
      return retval

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.count

  def _find_parent(self, index):
    return (index - 1) // 2

  def _find_child(self, index, lr = 0):
    if lr is 0:
      return self._index_exists((index * 2) + 1)
    if lr is 1:
      return self._index_exists((index * 2) + 2)

  def _bubble_up(self, index):
    if index is 0:
      return
    else:
      parent = self._find_parent(index)
      if self.storage[parent] < self.storage[index]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        return self._bubble_up(parent)
      else:
        return

  def _index_exists(self, index):
    if index > self.count -1:
      return None
    else:
      return index

  def _sift_down(self, index):
    if index >= len(self.storage) - 1:
      return
    else:
      l = self._find_child(index, 0)
      r = self._find_child(index, 1)
      s = None

      # finds out if left and right children exist
      # if one or the other exists swap var becomes childs index
      # if both exist and one is bigger, uses that index for swap
      # if neither exist we are done sifting
      if l is None and r is None:
        return
      elif r is not None and l is None:
        s = r
      elif r is None and l is not None:
        s = l
      elif self.storage[l] > self.storage[r]:
        s = l
      else:
        s = r

      # if storage[swap] is greater than storage[index]
      # flip them and recurse at storage index
      if self.storage[s] > self.storage[index]:
        self.storage[s], self.storage[index] = self.storage[index], self.storage[s]
        print(f'post swap: {self.storage}')# <-- Debugging
        return self._sift_down(s)

      else:
        return

        



#######################
# Testing Inheritence #
#######################
# test_parent = Heap()
# test_parent.storage = [100,19,36,17,12,25,5]
# print(test_parent.storage[test_parent._find_parent(1)])
# print(test_parent.storage[test_parent._find_parent(2)])
# print(test_parent.storage[test_parent._find_child(1,0)])
# print(test_parent.storage[test_parent._find_child(1,1)])
# print(test_parent.storage[test_parent._find_parent(4)])
# print(test_parent.storage[test_parent._find_parent(5)])
#########################################################

#####################
# Testing Insertion #
#####################
# test_insertion = Heap()
# print(test_insertion.storage)
# test_insertion.insert(110)
# print(test_insertion.storage)
# test_insertion.insert(10)
# print(test_insertion.storage)
# test_insertion.insert(1010)
# print(test_insertion.storage)
###############################

####################
# Testing Deletion #
####################
# test_delete = Heap()
# arr = [12,17,36,25,5,19,100]
# for i in arr:
#   test_delete.insert(i)
# print(f'before delete: {test_delete.storage}')
# print(f'delete result: {test_delete.delete()}')
# print(f'after delete: {test_delete.storage}'
#################################################