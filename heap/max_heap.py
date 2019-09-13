class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # pass
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    pass

  def get_max(self):
        # this is pretty straightfoward since the max should be at the top
        return self.storage[0]
    # pass

  def get_size(self):
        # this is also pretty straighfoward since we just need to find the len of the array
        return len(self.storage)
    # pass

  def _bubble_up(self, index):
    # pass
    # here we get teh index from the "insert" function from the top
    # and while it's larger then '0' which it usually is it will loop until it breaks
    while index > 0:
          # here with this mathmatical equation we can find the parent index

          # this is found starting by putting the tree as an array with it we can find the parent of each child with this function "2n+1" and "2n+2" since each node can only ever have two children
          # take this tree here
            #           20
            #     13          9
            #   8   5       3   7
            #  6 2
          # we can convert this into an array like so
          #  0  1  2 3 4 5 6 7 8 --> index
          # [20,13,9,8,5,3,7,6,2] we take each line of the tree as such and insert left to right
          # and with this array we can find the location of each parent's child
          # take index '2' for example which is '9' by putting '2' into the equation
          # 2n+1 so 2 * 2 + 1 we get the index of 5 which is 3 and with the 2n+2 we get index of 6 whic is 7
          # with the above tree we can see that 3 and 7 are both children of 9 so this equation works and opposite works as well with the number of the index we can divide it with (index -1)//2 which will give us our parent
          # so take the number 7 which has the index of 6 we input the equation 6-1/2 and floor it so it ends up as 2 which is the location of the number 9 and with the tree we can see it is indeed the index of the parent of that specified index

          parent = (index - 1)//2
          # with it we can now compair with the number at the current index with the parent index
          # if it's larger then the parent...
          if self.storage[index] > self.storage[parent]:
                # ...then we swap
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
          else:
                break

  def _sift_down(self, index):
    pass
