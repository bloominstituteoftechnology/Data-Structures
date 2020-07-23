#A linked list is a sequence of data items, just like an array. But where an array allocates a big block of memory to store the objects, the elements in a linked list are totally separate objects in memory and are connected through links:
#create Node

class Node:
    def __init__(self, value=none, next=none):
        self.value = value
        self.next = next
# _repr__() is used to compute the “official” string representation of an object
    def __repr__(self):
        return self.value
    def get_value(self):
        return self.value
    def get_next(self):
        return self.value
    def set_next(self, new_next):
        self.next = new_next

