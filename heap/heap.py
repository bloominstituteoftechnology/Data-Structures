class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    if len(self.storage) >= 2:
      self._bubble_up(index)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    print('\nlets bubble up this-------')
    parent_index = self._get_parent_index(index)
    print('index', index)
    print('parent index', parent_index)
    print(self.storage)
    print('--\n')
    while self.storage[parent_index] < self.storage[index]:
        print('begin while loop:')
        print('index', index)
        print(f'{self.storage[index]} is greater than {self.storage[parent_index]}. lets swap them')
        self._swap(index, parent_index)
        index = parent_index
        # tmp = self.storage[parent_index]
        # element = self.storage[parent_index]
        # self.storage[parent_index] = tmp
    print(self.storage)


  def _sift_down(self, index):
    pass

  def _get_parent_index(self, index):
    return index-2 // 2
  
  def _swap(self, index, parent_index):
    tmp = self.storage[index]
    self.storage[index] = self.storage[parent_index]
    self.storage[parent_index] = tmp



heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)