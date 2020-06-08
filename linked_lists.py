class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value

    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

#this is the hard way to make a linked list
linked_list = Node(1)
linked_list.next_node = Node(2)
linked_list.next_node.next_node = Node(3)

#another hard way to do this 

ll = Node(1)
ll_2 = Node(2)

ll.set_next(ll_2)
#and so on, and so forth

#Right now, it is hard to act on the list as a whole,
#so lets make this new class

class LinkedList:
    def __init__(self):
        self.head = None #first node in list
        #because we can only look at the beginning, we have to cycle through the whole list to get to the end
        self.tail = None

    #now we can directly add nodes to the list, no traversing
    #so now it is 0(1)
    def add_to_end(self, value):
        # what if the list is empty?
        # -- value is the actual value, not wrapped by node
        # -- wrap it in node and make it first in our list

        new_node = Node(value) # we should do this regardless if empty

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        
        # and not empty?
        else:
            #now we don't need to traverse the whole list

            #set the current tail's next to the new node
            self.tail.set_next(new_node)
            #set self.tail to the new node
            self.tail = new_node

    #we can directly remove this, no traversing
    #O(1)
    def remove_from_head(self):
        #what if the list is empty?
        # -- nothing to remove

        if not self.head:
            return None
        #what if the list isn't empty?
        else:
            #we want to return value at current head
            #also want to remove the value
            #and update self.head

            value = self.head.get_value()

            self.head = self.head.get_next()

            return value

    def add_to_head(self, value):
      new_node = Node(value)

      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node

      else:
        new_node.set_next(self.head)
        self.head = new_node

    def print_ll_elements(self):
      current = self.head

      while current is not None:
        print(current.value)
        current = current.get_next