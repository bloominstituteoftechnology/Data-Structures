from doubly_linked_list import DoublyLinkedList


#more specific to what we are doing, but can be refactored in Doubly Linked List Class

class LRUCache:

    def __init__(self, limit = 10):
        self.limit = limit
        self.size = 0 # if our LRUCache is separate
        self.storage = {}
        self.order = DoublyLinkedList()

    def get(self, key):
        # if key is in storage
        if self.key in self.storage[key]:
            # move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            return node.value[1] # returning tuple
        else:
            return
    
    def set(self, key, value):
        # if cache is not empty:
        if key in self.storage:
            # we write to a key value pair inside a linked list node, so we grab a node
            node = self.storage[key]
        # check and see if key is in dict
        # if it is 
            # overwrite the value
            node.value = (key, value) # or self.value, storing key value pairs
            # move it to the end, whichever end you want to use
            self.order.move_to_end(node)
            return
        # it key isn't in dict check to see if it is full
        if self.size == self.limit:
            # if cache is full
                # remove the oldest entry in the cache - the dictionary and linked list
                del self.storage[self.order.head.value[0]]
                self.order.remove_from_head() # we arbitrarily decided thet the head is the oldest entry
                self.size -= 1

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail # we put the whole node in dictionary
        # best way is to access data with more than one data structure

                # reduce the size

        # if the cache is empty
            # add to teh linked list key and value
            # add key and value to the dictionary
            # increment size

# to test, we can write an instance and print what's there
# 