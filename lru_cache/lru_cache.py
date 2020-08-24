class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def set_key(self, new_key):
        self.key = new_key
    
    def set_value(self, new_value):
        self.value = new_value
    
    def set_next(self, new_next):
        self.next = new_next
    
    def set_prev(self, new_prev):
        self.prev = new_prev


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.head = None
        self.tail = None
        self.storage_dict = {}
    
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage_dict:
            return None

        node = self.storage_dict[key]
        self.move_to_front(node)
        return node.get_value()

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
        if key in self.storage_dict:
            node = self.storage_dict[key]
            node.set_value(value)
            self.storage_dict[key] = node
            self.move_to_front(node)
            return

        if self.size >= self.limit:
            del self.storage_dict[self.tail.get_key()]
            self.remove_from_tail()
        
        new_node = Node(key, value)
        self.storage_dict[key] = new_node
        self.add_to_head(new_node)
    
    ######### Helper Methods #########
    
    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        list_str = ""
        curr = self.head
        while curr is not None:
            if curr is self.head:
                list_str += f"{curr.get_value()}"
            else:
                list_str += f" -> {curr.get_value()}"
            curr = curr.get_next()
        return f"Size = {self.size}, {{{list_str}}}\n"

    def delete(self, node):
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.size -= 1
            prev_node = node.get_prev()
            next_node = node.get_next()
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)
    
    def add_to_head(self, node):
        self.size += 1
        node.set_prev(None)
        node.set_next(self.head)
        if self.head:
            self.head.set_prev(node)
        else:
            self.tail = node
        self.head = node
    
    def remove_from_head(self):
        if self.isEmpty():
            return None
        
        self.size -= 1
        removed_value = self.head.get_value()
        self.head = self.head.get_next()
        if self.head:
            self.head.set_prev(None)
        else:
            self.tail = None
        return removed_value

    def remove_from_tail(self):
        if self.isEmpty():
            return None
        
        self.size -= 1
        removed_value = self.tail.get_value()
        self.tail = self.tail.get_prev()
        if self.tail:
            self.tail.set_next(None)
        else:
            self.head = None
        return removed_value
    
    def move_to_front(self, node):
        if node is not self.head:
            self.delete(node)
            self.add_to_head(node)