class Node:
    def __init__(self, value=name, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_node(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        # 0. create new node from value
        new_node = Node(value, None)
        # 1. check if list is empty
        if not self.head:
            # if list is empty, set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_head(self):
        if not self.head:
            return None
        # if head has no next...
        if not self.head.get_next:
            head = self.head
            # sety head reference to None
            self.head = None
            # set tail reference to None
            self.tail = None
            return head.get_value()
        value = self.head.get_value
        self.head = self.head.get_next()
        return value

        # 2. create a new node with value arg
        # 3. it depends  

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
        # update our current node to the current node's next node
        current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False