class Node:
  def __init__(self, value=None, next_node=None, prev_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
    self.prev_node = prev_node
  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def get_prev(self):
    return self.prev_node
    
  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

  def set_prev(self, new_prev):
    self.prev_node = new_prev 

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        self.tail = None 

    # O(1) 
    def add_to_head(self, value):
        # always first check if empty
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node 
        else:
            # we want to return the value at the current tail
            new_node.set_next(self.head)
            self.head = new_node
            # remove value at the tail
            # update

    # run time is now O(1) that we have tail and head     
    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            # no more traversals since we now keep first and last
            new_node.set_prev(self.tail)
            self.tail = new_node 

    # runs in O(1) since have access
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value

    def remove_from_tail(self):
        if not self.tail:
            return None 
        else:
            # we want to remove and return value at current tail
            value = self.tail.get_value()
            # remove value at tail and update self.tail
            self.tail = self.tail.get_prev()
            return value 

    def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()
    
    def print_ll_elements_reverse(self):
        current = self.tail

        while current is not None:
            print(current.value)
            current = current.get_prev()

a = LinkedList()

a.add_to_head(5)
a.add_to_head(15)
a.add_to_head(25)
a.print_ll_elements()


a.add_to_tail(35)
# print("Reverse Print")
# a.print_ll_elements_reverse()

a.print_ll_elements()