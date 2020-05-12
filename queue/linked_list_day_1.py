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

    # run time is now O(1) that we have tail and head     
    def add_to_end(self, value):
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
            self.tail.set_next(new_node)
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

a = LinkedList()

a.add_to_end(5)
a.add_to_end(15)
a.add_to_end(25)
print(a.remove_from_head())