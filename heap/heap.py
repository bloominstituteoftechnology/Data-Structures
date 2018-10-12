from math import floor, inf

class Heap:
  """
  Formulas!
  l = 2i + 1
  r = 21 + 2
  p = floor((i-2)/2)
  """
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    i = len(self.storage) - 1
    self._bubble_up(i)

  def delete(self):
    deleted_node = self.storage.pop(0)
    self._sift_down(0)
    return deleted_node

  def get_max(self):
    #return the root value
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    #index is the index of the element that will be moving up the heap
    #keep bubbling the element at the given index up the heap until it reaches a valid spot
    while (index - 1) // 2 >=0:
      #check to see if the element's parent value is less than the currrent value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        #swap the values
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
        #update the syntax to be the parent's index so that we can continue moving up the heap
        index = (index- 1) // 2 


  # def _sift_down(self, index):
    # #index is the index of the parent element
    # #compare the parent element's children with each other to determine larger element
    # while (index - 1) //2 >=0:
    # #compare the larger child element with parent to see if parent value is less than child value
    # child1 = self.storage[correct index]
    # child2 = self.storage[correct index]
    # #if child element value is larger, swap the values
    # #update the syntax so that we can continue sifting

    def _sift_down(self, index):
    # print('another sift down at index:', index)
      def swap_in_storage(i1, i2, lst=self.storage):
        temp = lst[i1]
        lst[i1] = lst[i2]
        lst[i2] = temp

    # indices
    left_i = 2 * index + 1
    right_i = 2 * index + 2
    max_i = self.get_size() - 1

    if index > max_i:
      return

    # values
    root = self.storage[index]
    left = self.storage[left_i] if left_i <= max_i else -inf
    right = self.storage[right_i] if right_i <= max_i else -inf
    # print('root:', root, 'left:', left, 'right:', right)


    if root < left and root < right:
      if left > right:
        swap_in_storage(index, left_i)
        self._sift_down(left_i)
      else:
        swap_in_storage(index, right_i)
        self._sift_down(right_i)
    elif root < left:
      swap_in_storage(index, left_i)
      self._sift_down(left_i)
    elif root < right:
      swap_in_storage(index, right_i)
      self._sift_down(right_i)