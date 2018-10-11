class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    index=self.get_size()
    self.storage.append(value)
    self._bubble_up(index)

  def delete(self):
    if self.get_size()>1:
      removed_head=self.storage[0]
      self.storage[0]=self.storage.pop()
      self._sift_down(0)
    else:
      removed_head=self.storage.pop()
    return removed_head

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index-1)//2>=0:
      if self.storage[index]>self.storage[(index-1)//2]:
        placeholder=self.storage[(index-1)//2]
        self.storage[(index-1)//2]=self.storage[index]
        self.storage[index]=placeholder
        index=((index)-1)//2
      else:
        break

  def _sift_down(self, index):
    length=self.get_size()
    while ((index+1)*2)<length:
      if self.storage[2*index+1]>=self.storage[2*index+2]:
        if self.storage[2*index+1]>self.storage[index]:
          placeholder=self.storage[2*index+1]
          self.storage[2*index+1]=self.storage[index]
          self.storage[index]=placeholder
          index=2*index+1
        else:
          break
      elif self.storage[2*index+2]>self.storage[2*index+1]:
        if self.storage[2*index+2]>self.storage[index]:
          placeholder=self.storage[2*index+2]
          self.storage[2*index+2]=self.storage[index]
          self.storage[index]=placeholder
          index=2*index+2
        else:
          break
      else:
        break