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
    if self.head == None: 
      current_node = Node(value)

    while current_node.next_node == None: 
        answer = int(input(f'Enter next node for {current_node.value} or type "quit": '))
        while True: 
          if answer == 'quit': 
            next_value = current_node.value
            break 
          # elif : 
          #   print('Invalid response. Please enter a number.')
          #   answer = input(f'Enter next node for {current_node.value} or type "quit": ')
          #   continue 
          
          current_node.set_next(int(answer))
          print('current_node.get_next', current_node.get_next)
          next_value = current_node.get_next
          break
    
    return next_value

  def remove_head(self):
    pass

  def contains(self):
    pass

  def get_max(self):
    pass

a = LinkedList()
b = a.add_to_tail(1)
print(b)
