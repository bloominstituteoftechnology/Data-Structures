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
      #create new node with passed value
      node_to_add = Node(value)
      #check if head->next is pointing to Null , means empty linked list if yes head and tail will be same
      if self.head == None:
          self.head = node_to_add
          self.tail = node_to_add
      else:
          self.tail.set_next(node_to_add)
          self.tail = node_to_add

  def remove_head(self):
      #check if the linked-list is empty .. return None
      if self.head == None:
          return None
      else:
          old_head_value = self.head.value
          if self.head.next_node is not None:
              self.head = self.head.next_node
          elif self.head.next_node is None:
              self.head = None
              self.tail = None
          return old_head_value

  def contains(self, value):
      current_node = self.head
      while True:
          if current_node == None:
              return False
          elif current_node.value == value:
              return True
          else:
              current_node = current_node.next_node

  def get_max(self):
      #check if the linked-list is empty .. return None
      if self.head == None:
          return None
      else:
          max = 0
          current = self.head
          while current != None:
            if current.get_value() > max:
                max = current.get_value()
            else:
                current = current.get_next()
        
      return max
      
  def display(self):
        current = self.head
        while current != None:
            print(current.get_value(), end = " -> ")
            current = current.get_next()
           
      
ll = LinkedList()
ll.add_to_tail(10)
ll.add_to_tail(20)
ll.add_to_tail(30)
ll.add_to_tail(40)
ll.add_to_tail(90)
ll.add_to_tail(129)
ll.add_to_tail(460)
ll.display()
print("\nMax in Linked- List  : ", ll.get_max())
print(ll.contains(460))
l5 = LinkedList()
l5.add_to_tail(1)
l5.add_to_tail(2)
l5.add_to_tail(5)
l5.add_to_tail(10)
l5.display()
print("****",l5.contains(10))
print(l5.contains(2))

print(l5.contains(1000))
