import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    if len(self.storage) > 1:
      self._bubble_up(len(self.storage)-1)

  def delete(self):
    value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage)-1]
    self.storage.pop(len(self.storage)-1)
    if len(self.storage) > 0:
      self._sift_down(0)
    return value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 1 or index == 2:
      parentIndex = 0
    else:
      parentIndex = math.floor((index-1)/2) #getParent(index)
    parent = self.storage[parentIndex]
    child = self.storage[index]
    if child > parent:
      #print('parent: ' + str(parent) + ', index: ' + str(parentIndex))
      #print('child: ' + str(child) + ', index: ' + str(index))
      self.storage[index] = parent
      self.storage[parentIndex] = child
      #print(self.storage)
      if(parentIndex != 0):
        self._bubble_up(parentIndex)

  def _sift_down(self, index):
    #print('')
    #print('--------: ' + str(index))
    #print(self.storage)

    children = []
    childrenIndices = [2*(index+1)-1,2*(index+1)]
    parent = self.storage[index]
    
    if childrenIndices[0] > self.get_size()-1:
      #done -- are no children
      pass
    else:
      if childrenIndices[1] > self.get_size()-1:
        #one child
        childrenIndices.pop(1)
      #get values
      for childIndex in childrenIndices:
        children.append(self.storage[childIndex])
      #children.reverse()
      if len(children) > 1:
        if children[0] < children[1]:
          children.reverse()
          childrenIndices.reverse()

      #now whether 1 or 2 children, max value child is in 0th position
      if children[0] > parent:
        self.storage[index] = children[0]
        #print('storage['+str(index)+']='+str(self.storage[index]))
        self.storage[childrenIndices[0]] = parent
        #print('storage['+str(childrenIndices[0])+']='+str(self.storage[childrenIndices[0]]))
        self._sift_down(childrenIndices[0])


#personal tests
'''
h = Heap()
h.insert(5)
print(h.storage)
h.insert(6)
print(h.storage)
h.insert(7)
print(h.storage)
h.insert(1)
print(h.storage)
h.insert(9)
print(h.storage)
h.insert(100)
print(h.storage)
h.delete()
print(h.storage)
'''