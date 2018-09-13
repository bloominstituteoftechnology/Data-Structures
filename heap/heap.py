class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # Add to end of heap, then compare to parents until correct order

  def delete(self):
    # Store the first element as rv, then put last element in first spot. Commpare with children until correct order

  def get_max(self):
    # Return first element in heap
    pass

  def get_size(self):
    # Return length of heap storage
    pass

  def _bubble_up(self, index):
    # Compare element with it's parent. If element is larger, then swap with parent
    pass

  def _sift_down(self, index):
    # Compare element's children. If one is larger, then swap. If both are larger, then take the larger one and swap.  
    pass
