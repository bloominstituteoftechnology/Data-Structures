class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
​
  def get_value(self):
    return self.value
​
  def get_next(self):
    return self.next_node
​
  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next
​
class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        # last node in the linked list 
        self.tail = None
​
    # O(1)
    def add_to_head(self, value):
        new_node = Node(value)
​
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.set_next(self.head)
            self.head = new_node
​
    # we have access to the end of the list, so we can directly add new nodes to it 
    # O(1)
    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head and not self.tail:
            # set both head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # set the current tail's next to the new node 
            self.tail.set_next(new_node)
            # set self.tail to the new node 
            self.tail = new_node
​
    # we already have access to the head of the linked list, so we can directly remove from it 
    # O(1)
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
​
    # iterate over our linked list and print out each value in it 
    def print_ll_elements(self):
        current = self.head
​
        while current is not None:
            print(current.value)
            current = current.get_next()
​
ll = LinkedList()
ll.add_to_head(3)
ll.add_to_head(5)
ll.add_to_head(9)
ll.add_to_head(11)
ll.print_ll_elements()