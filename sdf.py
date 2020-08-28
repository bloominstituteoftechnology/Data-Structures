# Print out all of the numbers in the following array that are divisible by 3:
my_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# The expected output for the above input is:
#   27
#   81
#   9
#   27
#   99
#   63
#   42
# Verbalize your thought process as much as possible before writing any code. Run through #  the UPER problem solving framework while going through your thought process.


for i in my_list:
    if i % 3 == 0:
        print(i)
# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""


# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             next_node = self.next
#             next_node.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     """Wraps the given value in a ListNode and inserts it
#     as the new head of the list. Don't forget to handle
#     the old head node's previous pointer accordingly."""

#     def add_to_head(self, value):
#         new_node = ListNode(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1

#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""

#     def remove_from_head(self):
#         # if self.head is None:
#         #     return None
#         head_value = self.head.value
#         self.delete(self.head)
#         return head_value
#         # if self.head is self.tail:
#         #     self.head = None
#         #     self.tail = None
#         #     self.length -= 1
#         #     return head_value
#         # else:
#         #     head = self.head
#         #     self.head = self.head.next
#         #     self.length -= 1
#         #     self.delete(head)
#         #     return head_value

#     """Wraps the given value in a ListNode and inserts it
#     as the new tail of the list. Don't forget to handle
#     the old tail node's next pointer accordingly."""

#     def add_to_tail(self, value):
#         new_node = ListNode(value)
#         self.length += 1
#         if not self.head and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node

#     """Removes the List's current tail node, making the
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""

#     def remove_from_tail(self):
#         # if self.tail is None:
#         #     return None
#         # tail_value = self.tail.value
#         # if self.head is self.tail:
#         #     self.head = None
#         #     self.tail = None
#         #     self.length -= 1
#         #     return tail_value
#         # else:
#         #     tail = self.tail
#         #     self.tail = self.tail.next
#         #     self.length -= 1
#         #     self.delete(tail)
#         #     return tail_value
#         tail_value = self.tail.value
#         self.delete(self.tail)
#         return tail_value

#     """Removes the input node from its current spot in the
#     List and inserts it as the new head node of the List."""

#     def move_to_front(self, node):
#         if node is self.head:
#             return
#         # if node is self.tail:
#         #     self.tail = self.tail.prev
#         #     self.delete(node)
#         else:
#             new_head = node.value
#             self.delete(node)
#             self.add_to_head(new_head)

#     """Removes the input node from its current spot in the
#     List and inserts it as the new tail node of the List."""

#     def move_to_end(self, node):
#         # if self.tail is None:
#         #     return None
#         if node is self.tail:
#             return
#         elif self.length == 1:
#             return
#         else:
#             new_tail = node.value
#             self.delete(node)
#             self.add_to_tail(new_tail)

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""

#     def delete(self, node):
#         if self.head is None and self.tail is None:
#             return
#         if self.head == self.tail and node == self.head:
#             self.head == None
#             self.tail == None
#         elif self.head == node:
#             self.head == node.next
#             node.delete()
#         elif self.tail == node:
#             self.tail == node.prev
#             node.delete()
#         else:
#             node.delete()
#         self.length -= 1

#     """Returns the highest value currently in the list"""

#     def get_max(self):
#         if not self.head and not self.tail:
#             return
#         if self.length == 1:
#             return self.head.value
#         else:
#             max_value = 0
#             value = self.head.value
#             current_value = self.head
#             while current_value is not None:
#                 if current_value.value > max_value:
#                     max_value = current_value
#                 current_value = current_value.next
#             return max_value
