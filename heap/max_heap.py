# python3 heap/test_max_heap.py -v

"""
Should have the methods insert, delete, get_max, _bubble_up, and _sift_down.
- insert adds the input value into the heap; this method should ensure 
         that the inserted value is in the correct spot in the heap
- delete removes and returns the 'topmost' value from the heap; 
         this method needs to ensure that the heap property is maintained after 
         the topmost element has been removed.
- get_max returns the maximum value in the heap in constant time.
- get_size returns the number of elements stored in the heap.
- _bubble_up moves the element at the specified index "up" the heap by swapping it 
         with its parent if the parent's value is less than the value at the specified index.
- _sift_down grabs the indices of this element's children and determines which child has a larger value. 
         If the larger child's value is larger than the parent's value, the child element is swapped with 
         the parent.
"""


class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        last = len(self.storage)-1
        self._bubble_up(last)

    def delete(self):
        if self.size > 1:
          max = self.storage.pop(0)
          self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
          self.size -=1
          self._sift_down(0)
        else:
          max = self.storage.pop(0)
          self.size -=1
        return max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        next = index + 1
        while index < (len(self.storage)-1):
            if next <= (len(self.storage)-1) and self.storage[next] <= self.storage[index]:
              next += 1
              self._sift_down(next)
            elif next <= (len(self.storage)-1) and self.storage[next] > self.storage[index]:
                self.storage[index], self.storage[next] = self.storage[next],self.storage[index]
            #   self._sift_down(next)
                self._sift_down(self.storage[0])
            else:
                break

# class Heap:
#     def __init__(self):
#         self.storage = [0]
#         self.size = 0

#     def insert(self, value):
#         self.storage.append(value)
#         self.size += 1
#         last = len(self.storage) - 1
#         self._bubble_up(last)

#     def delete(self):
#         last = len(self.storage) - 1
#         if self.size == 2:
#           self.size -=1
#           max = self.storage.pop(1)
#         elif self.size > 2:
#           max = self.storage.pop(1)
#           self.storage[1], self.storage[last-1] = self.storage[last-1],self.storage[1]
#           self.size -=1
#           self._sift_down(1)
#         else:
#           return False
#         return max

#     def get_max(self):
#         return self.storage[1]

#     def get_size(self):
#         return self.size

#     def _bubble_up(self, index):
#         parent = index // 2 
#         if index <= 1:
#           return
#         else:
#           if self.storage[index] > self.storage[parent]:
#             self.storage[index], self.storage[parent] = self.storage[parent],self.storage[index]
#             self._bubble_up(parent)
          
#     def _sift_down(self, index):
#         left_child = index * 2
#         right_child = index * 2 + 1
#         largest = index
#         if left_child < len(self.storage) - 1 and self.storage[left_child] > self.storage[index]:
#           largest = left_child
#           self.storage[index], self.storage[left_child] = self.storage[left_child],self.storage[index]
#           self._sift_down(largest)
#         elif right_child < len(self.storage) - 1 and self.storage[right_child] > self.storage[index]:
#           largest = right_child
#           self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
#           self._sift_down(largest)

