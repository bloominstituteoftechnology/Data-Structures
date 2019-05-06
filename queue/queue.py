class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        #Wrap the value in a new node
        new_node = Node(value)
        # 1. What if our linked list is empty? 
        # how do we even check if our linked list is empty
        if not self.head and not self.tail: 
            # if our list is empty, then the node that we add to the list needs
            # to be set as both the head and the tail
            self.head = new_node
            self.tail = new_node
        # 2. What if our linked list is not empty?
        else:
            # add to the tail of our list
            # update the tail node's next_node reference to point to the new node
            self.tail.set_next(new_node)
            # dont forget to update the linked'list's self.tail reference
            self.tail = new_node
            ## Must update the prior tail's next val then create the new tail

    def remove_head(self):
        # 1. What if our linked list is empty?
        if not self.head and not self.tail: 
            return None
        # 2. What if our linked list has a single node?
        elif self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None 
            return old_head.get_value()   
        # 3. What if our linked list has more than one node?
        else:
            # set the list's head reference to refer to the head node's next node
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def count(self):
      current = self.head
      count = 0
      while current:
        count += 1
        current = current.get_next()
      return count

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_to_tail(item)
  def dequeue(self):
    return self.storage.remove_head()
  def len(self):
    return self.storage.count()
