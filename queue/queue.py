"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self._size = 0
        self._storage = LinkedList()
    
    def __len__(self):
        return self._size

    def enqueue(self, value):
        self._storage.add_to_tail(value)
        self._size += 1

    def dequeue(self):
        if self.__len__() > 0:
            self._size -= 1
            return self._storage.remove_head()
        if self.__len__() <= 0:
            return


if __name__ == "__main__":
    pass

# import pkgutil
# search_path = ['.'] # set to None to see all modules importable from sys.path
# all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
# print(all_modules)

# Ran 4 tests in 0.000s
# OK