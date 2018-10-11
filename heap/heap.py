import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size()-1)

  def delete(self):
    val = self.storage[0]
    self.storage[0] = self.storage[self.get_size()-1]
    self.storage.pop()
    self._sift_down(0)
    return val

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    child = self.storage[index]
    newindex = math.floor((index-1)/2)
    if newindex < 0:
        newindex = 0
    parent = self.storage[newindex]
    if child > parent:
        self.storage[newindex] = child
        self.storage[index] = parent
        self._bubble_up(newindex)

  def _sift_down(self, index):
    end = self.get_size() - 1
    if index > end:
        return
    parent = self.storage[index]

    if end >= 2*index+1:
        lchild = self.storage[2*index+1]
    else:
        lchild = None
    if end >= 2*index+2:
        rchild = self.storage[2*index+2]
    else:
        rchild = None

    if not lchild and not rchild:
        return

    if lchild and not rchild:
        if parent < lchild:
            self.storage[index] = lchild
            self.storage[2*index+1] = parent
            if end >= 2*index+1:
                self._sift_down(2*index+1)

    if rchild and not lchild:
        if parent < rchild:
            self.storage[index] = rchild
            self.storage[2*index+2] = parent
            if end >= 2*index+2:
                self._sift_down(2*index+2)

    if lchild and rchild:
        if lchild > rchild and parent < lchild:
            self.storage[index] = lchild
            self.storage[2*index+1] = parent
            if end >= 2*index+1:
                self._sift_down(2*index+1)
        elif rchild >= lchild and parent < rchild:
            self.storage[index] = rchild
            self.storage[2*index+2] = parent
            if end >= 2*index+2:
                self._sift_down(2*index+2)
