# how do you find and return the middle node of a singly linked list in one pass?

# you do not have access to the length of the list, if the list is even, return first of two middle nodes
# you may not store in another data structure, including another linked list

# official question: How do you find and return 
# the middle node of a singly linked list in one pass? 
# You do not have access to the length of the list. 
# If the list is even, you should return the first 
# of the two “middle” nodes. You may not store the 
# nodes in another data structure.

# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import ListNode



# class LinkedList:
#     def __init__(self):
#         self.head = None


# if __name__ == '__main__':
#     l = [9,2,5,3,7,4,6,8,1]
#     llist = ListNode(l[0])
#     for i in l:
#         llist.insert_after(i)
#     print(llist.value)


#runtime to remove from head or tail O(1)

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class SinglyLinkedList:
  def __init__(self, value):
    first_node = Node(value)
    self.head = first_node
    self.tail = None
    # tail is none, run once

  def insert_into(self, value):# if tail is none, there's one element in singly linked list
    new_node = Node(value)# assign a tail, ie tail is new node if only 1 element in list
    if self.tail is None:
      self.tail = new_node
      self.head.next = new_node # head points to new node
    else: # if there is a tail, update tail's next property
      self.tail.next = new_node # update from none and point to new node
      self.tail = new_node # we insert into, we insert into tail
  #  self.head = new_node


def midpoint(sll):
  hare = sll.head # 
  turtle = sll.head
  while hare.next:
    if hare.next.next is None:
      return turtle.value
    hare = hare.next.next
    turtle = turtle.next
  return turtle.value


# Test it
sll = SinglyLinkedList(0)
for i in range(1, 51):
  # node = arr[i]
  sll.insert_into(i)

print("First value: ", sll.head.value)
print("Middle value: ", midpoint(sll)) # Works now
print("Last value: ", sll.tail.value)

# a variable is not a data structure

def findMiddle(double_list):
    # empty list
    if double_list.head == None:
        return None
    # only one item in list, return head node
    if double_list.head.next == None:
        return double_list.head
    # cache the current last item you have iterated to at
    last = double_list.head
    # cache the current middle of your traversed list
    middle = double_list.head
    # create a counter
    i = 1
    # iterate until you reach the tail, at which point last.next() will be False
    while last.next() == True:
        last = last.next()
        i += 1
        if i % 2 == 1:
            middle = middle.next()
    return middle

# ----------
mylist = Sin



# ---------
# in one pass reverse a linked list

#update the tail to be the head
# change the next to previous
def reverse_sll(sll):
    # create a prev_node variable to keep track of
    prev_node = None
    current_node = sll.head
    sll.tail = sll.head
    # initialized to none
    # loop over each node in sll
    while current_node is not None:
    # update current node next property to previous node
        current_node.next = prev_node
    # update previous node to the current node
        prev_node = current_node  # we need access to previous node
    # current node needs to be updated to current_node.next
        current_node = current_node.next
    # update the new tail
sll.tail = prev_node
sll.tail.next = None