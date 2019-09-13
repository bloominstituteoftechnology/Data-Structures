class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # pass
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    # pass
    # so first we have to see if the tree has any values in it
    if not self.storage:
          return False
    # if there is only one node in there then easy peasy we deletye
    elif len(self.storage) == 1:
          deleted = self.storage.pop()

    # if the tree has more then one
    elif len(self.storage) > 1:
          # we swap the top value with lowest value which is usually athe farthest right
          self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]

          # then we deleted the last value
          deleted = self.storage.pop()

          # and then we make sure the first value is the largest by sending in the first value in index '0' then that function will run shifting nodes until the highest value is at the top
          self._sift_down(0)
    else:
        deleted = False
    return deleted

  def get_max(self):
        # this is pretty straightfoward since the max should be at the top
        return self.storage[0]
    # pass

  def get_size(self):
        # this is also pretty straighfoward since we just need to find the len of the array
        return len(self.storage)
    # pass



  # this bubble up is mostly for when you first insert a node into to heaps
  def _bubble_up(self, index):
    # pass
    # here we get teh index from the "insert" function from the top
    # and while it's larger then '0' which it usually is it will loop until it breaks
    while index > 0:
          # here with a mathmatical equation we can find the parent index

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
          # 2n+1 so 2 * 2 + 1 we get the index of '5' which is '3' and with the 2n+2 we get index of '6' whic is '7'
          # with the above tree we can see that '3' and '7' are indeed both children of '9' so this equation works and opposite works as well with the number of the index we can divide it with (index -1)//2 which will give us our parent
          # so take the number '7' which has the index of '6' we input the equation 6-1/2 and floor it so it ends up as '2' which is the location of the number '9' and with the tree we can see it is indeed the index of the parent of that specified index

          parent = (index - 1)//2
          # with it we can now compair with the number at the current index with the parent index
          # if it's larger then the parent...
          if self.storage[index] > self.storage[parent]:
                # ...then we swap
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # then we reassign the child's index with the parents index, if not then child is at it's valid spot and we stop
                index = parent
          else:
                # with this break
                break


# while this function is when adjusting or deleting a node on a heap tree
# the main funcationality of this...well function is to check if the child is larger then the parent, if it is then swap the nodes.
  def _sift_down(self, index):
    # pass
    # here we first set variables to find the index and it's children like the equation above we can find it with the '2n+1' and '2n+2'
    max = index
    left_of_max = (index * 2) + 1
    right_of_max = (index * 2) + 2

    # so first we check the left side
    # if so then we switch out the max with the current index
    # if the current index AND the value at the index on the left of max is both less then the lenght of the storage AND the value of the index of the child then swap the max value
    if len(self.storage) > left_of_max and self.storage[max] < self.storage[left_of_max]:
      max = left_of_max

    # and now we check the right
    # and the same goes here
    if len(self.storage) > right_of_max and self.storage[max] < self.storage[right_of_max]:
      max = right_of_max

    # now if the max is not equal to the given index then the parent is not the highest value and therefore it is swapped and since we have to keep checking on EVERY parent we recursivly call the function to run again but this time we insert the current max value
    if max != index:
      self.storage[index], self.storage[max] = self.storage[max], self.storage[index]

      self._sift_down(max)