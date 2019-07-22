class Node:

    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    # returns number/ string/ etc.
    def get_value(self):
        return self.value

    # returns node object
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_value(self, value):
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #wrap value in a node
        new_node = Node(value)
        # check if we're in an empty list state
        if not self.head and not self.tail:
            #set the list's head reference to point to new_node
            self.head = new_node
            #set the list's tail reference to point to new_node
            self.tail = new_node
        else:
            # update the old tail's next reference to refer to the new node
            self.tail.set_next(new_node)
            # update the LinkedList's tail reference
            self.tail = new_node
        
    def add_to_head(self, node):
        # empty list
        if head == None:
            self.head = node
            self.tail = node
        #not empty
        else:
            node.set_next(self.head)
            self.head = node

    def remove_from_head(self):
        val = None
        #empty list
        if self.head == None:
            return None

        #removing only item in Linked list of 1
        elif self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
        
        #removing from linked list of 2+ items
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
        return val

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
    # `enqueue` should add an item to the back of the queue.
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
    # `dequeue` should remove and return an item from the front of the queue.
        if self.size == 0:
            return None

        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
    # `len` returns the number of items in the queue.
        return self.size
