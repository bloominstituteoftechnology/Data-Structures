"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
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
    new_node = Node(value)
    if not self.head:
        self.head = new_node
        self.tail = new_node
        return
    else:
        self.tail = new_node
        return

  def remove_head(self):
    if self.head:
            self.head = self.head.get_next()
            self.tail = None
            return self.head.value

  def contains(self, value):
    if self.head == None:  # if no nodes exists
            return False
        else:
            current_node = self.head
            while current_node is not None:  # if a node exists
                if (
                    current_node.value == value
                ):  
                    return True
                current_node = (
                    current_node.next_node
                )  
            return False  # no node has that argument value


  def get_max(self):
    if self.head == None:  # if no node exists
            return None
        else:
            current_node = self.head
            max_value = 0
            while current_node is not None:
                if (
                    current_node.value > max_value
                ): 
                    max_value = current_node.value  # update max_value
                    current_node = (
                        current_node.next_node
                    )  # keep going until reaches end
            return max_value
