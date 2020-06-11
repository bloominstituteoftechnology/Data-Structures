from typing import Optional
import math

class Heap:
    def __init__(self):
        self.storage = []
 
    def insert(self, value):
        self.storage.append(value)
        print(f"Array after insert {self.storage}")
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        size = len(self.storage)
        if size == 0:
            return None
        elif size == 1:
            return self.storage.pop(0)
        else:
            deleted = self.storage[0]
            self.storage[0] = self.storage.pop(-1)
            print(f"Array after deleting head and replacing with tail {self.storage}")
            self._sift_down(0)
            return deleted

    def get_max(self):
        return self.storage[0] if len(self.storage) > 0 else None

    def get_size(self):
        return len(self.storage)

    def _parent_index(self, index) -> Optional[int]:
        parent_index = math.floor((index - 1) / 2) 
        return parent_index if parent_index >= 0 else None
    
    def _left_child_index(self, index) -> Optional[int]:
        left_child_index = (index * 2) + 1
        return left_child_index if left_child_index < len(self.storage) else None

    def _right_child_index(self, index) -> Optional[int]:
        right_child_index =  (index * 2) + 2
        return right_child_index if right_child_index < len(self.storage) else None

    def _bubble_up(self, index):
        parent = self._parent_index(index)

        if parent is not None and self.storage[parent] < self.storage[index]:
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
            print(f"Array after bubbling up from index {index} to index {parent} {self.storage}")
            self._bubble_up(parent)

    def _sift_down(self, index):
        print("Sifting down")
        left_child = self._left_child_index(index)
        right_child = self._right_child_index(index)

        largest_child: Optional[int] = None

        if left_child and right_child:
            largest_child = left_child if self.storage[left_child] > self.storage[right_child] else right_child
        elif left_child:
            largest_child = left_child
        elif right_child:
            largest_child = right_child

        if largest_child and self.storage[largest_child] > self.storage[index]:
            self.storage[largest_child], self.storage[index] = self.storage[index], self.storage[largest_child]
            print(f"Array after sifting down from index {index} to index {largest_child} {self.storage}")
            self._sift_down(largest_child)




        







    