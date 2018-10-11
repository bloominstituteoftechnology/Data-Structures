class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    if not self.storage
        return None
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index-1)//2>=0:

        if self.storage[index-1)//2] < self.storage[index]:
            #swap values
            self.storage[index], self.storage[index-1)//2]=self.storage[index-1)//2], self.storage[index]
        
        index=(index-1)//2 #update the index to parent's index to keep moving up

  def _sift_down(self, index):
      while (2*index+2) >=0 and <=len(self.storage):
          left_index=2*index+1
          right_index=2*index+2

          if self.storage[left_index] > self.storage[index]:
              #swap values
              self.storage[index], self.storage[left_index]=self.storage[left_index], self.storage[index]
              index=left_index
          else self.storage[right_index] > self.storage[index]:
              #swap values
              self.storage[index], self.storage[right_index]=self.storage[right_index], self.storage[index]
              index=right_index
        
