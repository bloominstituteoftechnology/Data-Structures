import heapq

class Heap:
  def __init__(self):
    self.storage = []
    heapq.heapify(self.storage)

  def insert(self, value):
    return heapq.heappush(self.storage, value)

  def delete(self):
    return heapq.heappop(self.storage)


  def get_max(self):
    return heapq._heapify_max(self.storage)

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass
