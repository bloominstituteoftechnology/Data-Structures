class Heap:
  def __init__(self):
    self.storage = []
    self.size=0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)
    self.size+=1

  def delete(self):
    #print(f"Storage 0  {self.storage[0]}")
    #print(f"Storage last  {self.storage[-1]}")
    if len(self.storage)==1:
      self.size-=1
      return self.storage.pop()
      
    else:
      if len(self.storage)==0:
        return None
      else:
        temp=self.storage[0]
        self.storage[0]=self.storage.pop()
        self._sift_down(0)
        self.size-=1
        return temp
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    parent_index= (index-1) //2
    current_index= index
    while parent_index >= 0:
      if self.storage[parent_index]< self.storage[current_index]:
        self.storage[parent_index], self.storage[current_index]= self.storage[current_index], self.storage[parent_index]
      else:
        break
      current_index=parent_index
      parent_index= (parent_index-1) //2

  def _sift_down(self, index):
    current_index=index
    checker=False
    while not checker:
      if ((current_index*2)+1)> len(self.storage)-1 or ((current_index*2)+2)> len(self.storage)-1:
        if ((current_index*2)+1)> len(self.storage)-1:
          break
        else:
          if self.storage[(current_index*2)+1]> self.storage[current_index]:
            self.storage[(current_index*2)+1], self.storage[current_index]=self.storage[current_index],self.storage[(current_index*2)+1]
          else:
            checker=True
      elif self.storage[(current_index*2)+1]> self.storage[(current_index*2)+2]:
        if self.storage[(current_index*2)+1]> self.storage[current_index]:
          self.storage[(current_index*2)+1], self.storage[current_index]=self.storage[current_index],self.storage[(current_index*2)+1]
        else:
          checker=True
      elif self.storage[(current_index*2)+2]>= self.storage[(current_index*2)+1]:
        if self.storage[(current_index*2)+2]> self.storage[current_index]:
          self.storage[(current_index*2)+2], self.storage[current_index]=self.storage[current_index],self.storage[(current_index*2)+2]
        else:
          checker=True

