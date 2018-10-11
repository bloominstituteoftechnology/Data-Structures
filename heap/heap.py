class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    pass

  def get_max(self):
    print('self.storage:', self.storage)
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    current_value = self.storage[index]
    parent_value = self.storage[(index - 1) // 2]
    while index >= 0:
      if current_value > parent_value:
        self.storage[index] = parent_value 
        self.storage[(index - 1) // 2] = current_value
        index = (index - 1) // 2

  # def _sift_down(self, index):
  #   first_child = self.storage[2 * index + 1 ]
  #   second_child = self.storage[2 * index + 2 ]
  #   while self.storage[index] < first_child or second_child:
  #     better_child = first_child >


      
