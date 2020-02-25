class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class SinglyLinkedList:
  def __init__(self, value):
    first_node = Node(value)
    self.head = first_node
    self.tail = None

  def insert_into(self, value):
    new_node = Node(value)
    if self.tail is None:
      self.tail = new_node
      self.head.next = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
  #  self.head = new_node


# def midpoint(sll):
#   hare = sll.head
#   turtle = sll.head
#   while hare.next:
#     if hare.next.next is None:
#       return turtle.value
#     hare = hare.next.next
#     turtle = turtle.next
#   return turtle.value

def reverse_sll(sll):
  # Create a prev_node var to keep track of the previous node
  prev_node = None
  current_node = sll.head
  sll.tail = sll.head
  # Loop over each node in sll
  while current_node is not None:
    # update current node next property to be the prev_node
    current_node.next = prev_node
    if prev_node:
      print(prev_node.value)
    print(current_node.value)
    # Update prev_node to be the current_node
    prev_node = current_node # sll.head
    # current_node needs to be updated to be current_node.next
    current_node = current_node.next # second item
  # Update the new head
  sll.head = prev_node  # The problem was here I think was updating tail not head
  # sll.head.next = prev
  # return sll


sll = SinglyLinkedList(0)
for i in range(1, 51):
  # node = arr[i]
  sll.insert_into(i)

# print("First value: ", sll.head.value)
# print("Middle value: ", midpoint(sll)) # Works now
# print("Last value: ", sll.tail.value)

# Yeah, missing some logic
reverse_sll(sll)
print("First value(should be 50): ", sll.head.value)

# working version: 

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class SinglyLinkedList:
  def __init__(self, value):
    first_node = Node(value)
    self.head = first_node
    self.tail = None

  def insert_into(self, value):
    new_node = Node(value)
    if self.tail is None:
      self.tail = new_node
      self.head.next = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
  #  self.head = new_node


def midpoint(sll):
  hare = sll.head
  turtle = sll.head
  while hare.next:
    if hare.next.next is None:
      return turtle.value
    hare = hare.next.next
    turtle = turtle.next
  return turtle.value

def reverse_sll(sll):
  # Create a prev_node var to keep track of the previous node
  prev_node = None
  current_node = sll.head
  sll.tail = current_node
  # Loop over each node in sll
  while current_node is not None:
    next_node = current_node.next # This is what was missing
    # update current node next property to be the prev_node
    current_node.next = prev_node
    print(f"current node value: {current_node.value}")
    # Update prev_node to be the current_node
    prev_node = current_node # sll.head
    # current_node needs to be updated to be current_node.next
    current_node = next_node # this is wrong
  # Update the new head
  sll.head = prev_node  # The problem was here I think was updating tail not head
  # sll.head.next = prev
  # return sll

# Test it
sll = SinglyLinkedList(0)
for i in range(1, 51):
  # node = arr[i]
  sll.insert_into(i)

# print("First value: ", sll.head.value)
# print("Middle value: ", midpoint(sll)) # Works now
# print("Last value: ", sll.tail.value)

# Yeah, missing some logic
reverse_sll(sll)
print("First value(should be 50): ", sll.head.value)

# It's working e

# one solution

def reverse_one_pass(mylist):
    prev = None
    current = mylist.head
    while current.next == None:
        current.next, prev, current = prev, current, current.next