class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None
        self.count = 0
    
    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if self.head is None or self.tail is None:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
            self.count = 1
        # if we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node
            self.count += 1
    
    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no text, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise, we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        self.count -= 1
        return value
    
    def remove_tail(self):
      # if we have a non-empty linked list
      if self.head is None and self.tail is None:
          return
      # move self.tail to the Node right before
      # we have to start at the head and move down the linked list
      # until we get to the node right before the tail
      # iterate over our linked list
      current = self.head

      while current.get_next() is not self.tail:
          current = current.get_next()
      # at this point, `current` is the node right before the tail
      # set the tail to be None
      val = self.tail.get_value()
      self.tail = None
      self.count -= 1
      # move self.tail to the Node right before
      self.tail = current
      return val
    
    def contains(self, value):
        if not self.head:
            return False
        
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next_node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False
    
    def get_max(self):
      if self.head == None:
        return
      else:
        current = self.head
        max = 0
        
        while current is not None:
          if current.value > max:
            max = current.value
          else:
            current = current.get_next()
      return max
