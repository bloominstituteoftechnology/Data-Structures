class Heap:
  def __init__(self):
    self.storage = []
    # TODO: add a size var to keep track

  def insert(self, value):
    # append value to storage
    #increment size
    # bubble up
    pass

  def delete(self):
    # if empty return none

    # create variables for the storage top and storage end
    # decrement the size
    # if size zero return storage top

    # set storage of index 1 to storage end
    # shift down
    #return storage top
    pass

  def get_max(self):
    # return the storage at index 1
    pass

  def get_size(self):
    # return size
    pass

  def _bubble_up(self, index):
    # set index of parent to index divided by 2 ( as whole number ) see : https://www.geeksforgeeks.org/division-operator-in-python/
    # if the parent index is equal to zero return to the caller

    # if the storage at the index of parent is less than the storage of index swap the parent with the current node
    # and do a recursive call to bubble up at index of parent
    pass

  def _sift_down(self, index):
    pass