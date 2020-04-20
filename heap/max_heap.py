class Heap:
    def __init__(self):
        self.storage = []

"""
Heaps should have the methods insert, delete, get_max, _bubble_up, and _sift_down.
* insert adds the input value into the heap; this method should ensure that the inserted 
value is in the correct spot in the heap 
* delete removes and returns the ‘topmost’ value from the heap; this method needs to ensure 
that the heap property is maintained after the topmost element has been removed. 
*get_max returns the maximum value in the heap in constant time. 
* get_size returns the number of elements stored in the heap.
* _bubble_up moves the element at the specified index “up” the heap by swapping it with its 
parent if the parent’s value is less than the value at the specified index.
* _sift_down grabs the indices of this element’s children and determines which child has a 
larger value. If the larger child’s value is larger than the parent’s value, the child 
element is swapped with the parent.
"""

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
