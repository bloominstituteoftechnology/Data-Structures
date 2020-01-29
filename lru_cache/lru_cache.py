# import sys          -- dont need local file
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        # do first so we can get something
        # CREATE A NODE IF KEY NOT FOUND AND MOVE TO FRONT
        # MOVE NODE TO FRONT I KEY FOUND
        # IF FULL, REMOVE LAST NODE FROM THE LL AND DICT


        if key in self.storage:
            # access in middle of linked list by using key for dictionary
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # if its already full
        if self.size == self.limit:
            # zero first item in tuple
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1

        # if first data added -- give tuple with key and value
        self.order.add_to_tail((key, value))
        # SINCE WE HAVE SIZE, WE KNOW WE WILL AD TO IT
        # add to dictionary
        self.storage[key] = self.order.tail
        self.size += 1

