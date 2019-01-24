class Heap:
  def __init__(self):
    self.storage = []
    self.count = 0

  def insert(self, value):
    index = self.count
    self.storage.append(value)
    print(self.storage)
    self._bubble_up(index)
    self.count += 1

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _find_parent(self, index):
    return (index - 1) // 2

  def _find_child(self, index, lr = 0):
    if lr is 0:
      return (index * 2) + 1
    if lr is 1:
      return (index * 2) + 2

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

  def _sift_down(self, index):
    pass


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