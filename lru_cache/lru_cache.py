import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# benefits of linked list and hash table to create an index, if you want to grab somethign from the middle you can. 

# since python works as pass by reference
# you can have two data structures pointing to the same data without a meaningful increase in overhead

# class LRUCache:
#     """
#     Our LRUCache class keeps track of the max number of nodes it
#     can hold, the current number of nodes it is holding, a doubly-
#     linked list that holds the key-value entries in the correct
#     order, as well as a storage dict that provides fast access
#     to every node stored in the cache.
#     """
#     def __init__(self, limit=10):
#         self.limit = limit
#         self.size = 0 
#         self.storage = dict()
#         self.order = DoublyLinkedList()

#     """
#     Retrieves the value associated with the given key. Also
#     needs to move the key-value pair to the end of the order
#     such that the pair is considered most-recently used.
#     Returns the value associated with the key or None if the
#     key-value pair doesn't exist in the cache.
#     """
#     def get(self, key):
#         if key in self.storage:
#             node = self.storage[key]
#             self.order.move_to_end(node)
#             return node.value[1]
#         else:
#             return

#     """
#     Adds the given key-value pair to the cache. The newly-
#     added pair should be considered the most-recently used
#     entry in the cache. If the cache is already at max capacity
#     before this entry is added, then the oldest entry in the
#     cache needs to be removed to make room. Additionally, in the
#     case that the key already exists in the cache, we simply
#     want to overwrite the old value associated with the key with
#     the newly-specified value.
#     """
#     def set(self, key, value):
#         if key in self.storage:
#             node = self.storage[key]
#             node.value = (key,value)
#             self.order.move_to_end(node)
#             return
#         else:
#             if self.size == self.limit:
#                 del self.storage[self.order.head.value[0]]
#                 self.order.remove_from_head()
#                 self.size -= 1
#         self.order.add_to_tail(key, value)
#         self.storage[key] = self.order.tail
#         self.size += 1


# Further practice

# The doubly linked list is served as the value for our dictionary. 

# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.dict = dict()
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key): 
#         if key in self.dict: # if there is a key in the dictionary
#             node = self.dict[key]
#             self._remove(node) # we remove
#             self._add(node) # we add back in
#             return node.value
#         return -1 # if there is no key

#     def put(self, key, value):
#         if key in self.dict: # to refresh it, we have to remove it
#             self._remove(self.dict[key])
#             node = Node(key, value)
#             self.add_to_tail(node) # add to linked list
#             self.dict[key] = node# make the dictionary value equal to node
#             if len(self.dict) > self.capacity:
#                 node = self.head.next
#                 self._remove(node)
#                 del self.dict[node.key]

#     def _remove(self, node):
#         prev = node.prev
#         next = node.next
#         prev.next = next
#         next.prev = prev

#     def _add(self, node):
#         prev = self.tail.prev
#         prev.next = node
#         self.tail.prev = node
#         node.prev = prev
#         node.next = self.tail


# # ---------

# class LRUCache:

#     def __init__(self, limit=10):
#         self.limit = limit
#         self.size = 0
#         self.storage = dict()
#         self.order = DoublyLinkedList()

#     def get(self, key):
#         if self.key == None:
#             return
#         else:
#             #retrieve value associated with given key
#             node = self.storage[key]
#             # move key value pair to end of order
#             self.order.move_to_end(node)
#             # returns the value associated with the key
#             return node.value[1]


#     def set(self, key, value):
#         # The newly-added pair should be considered the 
#         # most-recently used entry in the cache.
#         if key in self.storage:
#             node = self.storage[key]
#             node.value = (key, value)
#             self.order.move_to_end(node)
#             return 
#         # If the cache is already at max capacity before 
#         # this entry is added
#         elif self.limit == self.size:
#             del self.storage[self.order.head.value[0]]
#             # then the oldest entry in the cache needs to be 
#             # removed to make room. 
#             self.order.remove_from_head()
#             self.size -= 1
#         # add to the linked list the key and value
#         self.order.add_to_tail(key, value)
#         # add key and value to dictionary
#         self.storage[key] = self.order.tail
#         self.size += 1

class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

    def get(self, key):
        # If key is in storage
        if key in self.storage:
            # move key to end
            node = self.storage[key]
            self.order.move_to_end(node)
            #return value
            return node.value[1]
        # If key is not in storage, return none
        else:
            return None



    def set(self, key, value):

    # If cache is not empty:
        # Check and see if the key is in the dictionary, if dictionary is empty key won't be there
        if key in self.storage:
            # If key is in dict
            node = self.storage[key] # grabbing the full node, if you store whole node in dictionary, you can grab it freely
                # Overwrite the value
            node.value = (key, value)
                # Move it to the end
            self.order.move_to_end(node)
            return

    # If key is not in dict
        # Check and see if cache is full
        if self.size == self.limit: # we get rid of the least recently used one, less likely that it is needed soon, but dictionary - you grab from anywhere
        # If cache is full
            # Remove oldest entry from dictionary and Linked List
            del self.storage[self.order.head.value[0]]
            #delete from linked list
            self.order.remove_from_head()# we arbitrarily decided that the head is the oldest entry
            # Reduce the size
            self.size -= 1

            # If the cache is empty
            # Add to the linked list (key and value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail # references is just a pointer, very low overhead, accessing data with different datatypes is efficient
        # Increment size
        self.size += 1
