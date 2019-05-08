class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    print(f'arr:{self.storage}')
    self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
    x = self.storage.pop()
    self._sift_down(0)
    # print(f'x:{x}')
    return x

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index-1)//2
      if self.storage[parent] < self.storage[index]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        index = parent
      else:
        break

  def _sift_down(self, index):
    loop = True
    while loop == True:
      left = 2*(index) + 1
      right = 2*(index) + 2
      print(f'index:{index}')
      print(f'left:{left}')
      print(f'right:{right}')
      arr = self.storage
      length = len(arr)-1
      print(f'length:{length}')

      if left <= length and right <= length:
        if arr[left] >= arr[index] and arr[left] >= arr[right]:
          arr[left], arr[index] = arr[index], arr[left]
          index = left
        elif arr[right] >= arr[index] and arr[left] < arr[right]:
          arr[right], arr[index] = arr[index], arr[right]
          index = right
        else:
          loop = False
      elif left <= length and right > length:
        if arr[left] >= arr[index]:
          arr[left], arr[index] = arr[index], arr[left]
          index = left
        else:
          loop = False
      elif right <= length and left > length:
        if arr[right] >= arr[index]:
          arr[right], arr[index] = arr[index], arr[right]
          index = right
        else:
          loop = False
      else:
        loop = False
