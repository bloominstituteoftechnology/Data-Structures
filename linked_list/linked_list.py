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
    self.new_node = None 
    self.middle_node_count = 1
    self.linked_list = {
      'head': {
        'value': None,
        'next': None
      }, 
      'tail': {
        'value': None, 
        'next': None 
      }
    }

  def add_to_tail(self, value): 
    if self.head == None: 
      self.head = Node(value)
      self.linked_list['head']['value'] = self.head.value
      self.linked_list['head']['next'] = self.head.next_node
      self.tail = self.head
      self.linked_list['tail']['value'] = self.tail.value 
      self.linked_list['tail']['next'] = self.tail.next_node
      print(f'The head is equal to {self.head.value}.')
      print(f'The first tail is equal to {self.tail.value}.')
    elif self.head.next_node == None:
      self.head.set_next(Node(value))
      self.new_node = Node(self.head.get_next().value)
      self.linked_list['Middle_Node{}'.format(self.middle_node_count)] = {'value': self.new_node.value, 'next': None}
      self.linked_list['head']['next'] = self.linked_list['Middle_Node{}'.format(self.middle_node_count)]
      self.tail = self.new_node
      self.linked_list['tail']['value'] = self.tail.value
      self.linked_list['tail']['next'] = self.tail.next_node
      print(f'The next value after the head is equal to {self.tail.value}.')
    elif self.new_node != None:  
      if self.new_node.next_node == None: 
        self.new_node.set_next(Node(value))
        self.new_node = Node(self.new_node.get_next().value)
        self.linked_list['Middle_Node{}'.format(self.middle_node_count+1)] = {'value': self.new_node.value, 'next': None}
        self.linked_list['Middle_Node{}'.format(self.middle_node_count)]['next'] = self.linked_list['Middle_Node{}'.format(self.middle_node_count+1)]
        self.middle_node_count += 1 
        self.tail = self.new_node
        self.linked_list['tail']['value'] = self.tail.value
        self.linked_list['tail']['next'] = self.tail.next_node
      print(f'The next value is {self.tail.value}.')
  
  def remove_head(self):
    pass
    # print('Self head value', self.head.value)
    # print('Self head next node.', self.head.next_node)

    # self.head.value = self.head.next_node.value
    # print(self.head.next_node.next_node); 
    # self.head.set_next(self.head.next_node.next_node)  

    # print('New head value', self.head.value)
    # print('New head next node', self.head.next_node)

  def contains(self):
    pass

  def get_max(self):
    pass

a = LinkedList()
a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.add_to_tail(7)
a.add_to_tail(8)
a.add_to_tail(9)
a.add_to_tail(10)
a.add_to_tail(11)
a.add_to_tail(12)

