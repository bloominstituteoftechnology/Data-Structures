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
    while index*2+1<length:
      max_child=self.get_max_child(index)
      if self.storage[max_child]>self.storage[index]:
        placeholder=self.storage[max_child]
        self.storage[max_child]=self.storage[index]
        self.storage[index]=placeholder
      index=max_child
  
  def  get_max_child(self,index):
    if index*2+2>self.get_size()-1:
      return index*2+1
    else:
      return index*2+1 if self.storage[index*2+1]>self.storage[index*2+2] else index*2+2