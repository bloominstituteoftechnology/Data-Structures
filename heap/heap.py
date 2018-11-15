#https://www.tutorialspoint.com/python/python_heaps.htm
#Heap is a special tree structure in which each parent node is less 
# than or equal to its child node. Then it is called a Min Heap. If each 
# parent node is greater than or equal to its child node then it is called 
# a max heap. It is very useful is implementing priority queues where the queue 
# item with higher weightage is given more priority in processing.

#Just remeber we are turning the heap into an array
import heapq

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    heapq.heappush(self.value)

  def delete(self):
    #remove item at first index
    heapq.heappop(self.storage)

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    pass

  def _sift_down(self, index):
    pass


# Create a Heap
# A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various operations on heap data structure. Below is a list of these functions.
# heapify - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
    # H = [21,2,3,7,4,88,23,100,42]
    # Convert to a Heap
    # heapq.heapify(H)
    # print(H)
    # //op [2,3,4,7,21,23,42,88,100]
# heappush – This function adds an element to the heap without altering the current heap.
# heappop - This function returns the smallest data element from the heap.
# heapreplace – This function replaces the smallest data element with a new value supplied in the function.