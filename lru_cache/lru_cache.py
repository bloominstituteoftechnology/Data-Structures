
from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #node limit to limit ^
        self.nodeLimit = limit
        #start the count
        self.nodeCount = 0
        # start the dictionary
        self.dict = dict()
        # link the list
        self.linkedList = DoublyLinkedList()
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # set current node to none 
        currentNode = None
        # point to the top of the linked list
        node = self.linkedList.head
        if node == None:
            return
        # while nothing in current node 
        while currentNode == None:
            # and there is a value in the node 
            if node.value == key:
                #then set the current node to it
                currentNode = node
                # then go to the next one 
            node = node.next
                # and once there no more node 
            if node == None:
                # break for while statement
                break
                # if nothing else to check
        if currentNode == None:
            return
                # then move the current node 
                #to the front of the list
        self.linkedList.move_to_front(currentNode)
                # and finally return
        return self.dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # now after getting the key
        # add the value to the cache 
        # null check:
        if self.get(key) != None:
            # then set the default key
            self.dict[key] = value

            # # if cache is not full:
        elif self.nodeCount != self.nodeLimit:
            # incremnt it 
            self.nodeCount += 1
            # assign it the value for cache and dictionary
            self.dict[key] = value
            # and the linked list 
            self.linkedList.add_to_head(key)
        else:
            # declare item to remove the item from the tail
            remove_the_item = self.linkedList.tail
            # then delete from tail of dictionary
            self.dict.pop(remove_the_item.value)
            # and also from tail of the list
            self.linkedList.delete(remove_the_item)
            # assign it the value for cache and dictionary
            self.dict[key] = value
            # and the linked list 
            self.linkedList.add_to_head(key)

            