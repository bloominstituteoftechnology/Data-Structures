# def add_to_head(self, value):
#     node = ListNode(value)
#
#     # DLL is empty
#     if self.head is None and self.tail is None:
#         self.head = node
#     # If head points to a node & tail points to none
#     else:
#         # point the tail to what the head is currently pointing at
#         self.tail = self.head
#         # point the head to the new node
#         self.head = node
#         # head -> | node node.next | -> tail
#         self.head.next = self.tail
#
#         self.tail.prev = self.head
#     self.length += 1


# def move_to_front(self, node):
#     itr = self.head
#
#     while itr:
#         if node == itr.value:
#             if self.length == 1:
#                 return
#             elif node == self.tail and self.length == 2:
#                 # swap the head and tail
#                 self.tail = self.head
#                 self.head = node
#                 self.head.next = self.tail
#                 self.head.prev = None
#                 self.tail.next = None
#                 self.tail.prev = self.head
#             else:
#                 # store the current iteration
#                 # found_value = itr.value
#                 self.delete(itr)
#                 self.add_to_head(node)
#
#         itr = itr.next

# def move_to_front(self, node):
#     # if node == head,
#     if node == self.head:
#         # do nothing, because the head is already at the front
#         return
#     # only head and tail exist
#     elif self.length == 2:
#         # swap head and tail
#         self.head = self.tail
#         self.tail = self.head.prev
#         self.tail.next = None
#         self.tail.prev = self.head
#         self.head.next = self.tail
#         self.head.prev = None
#     elif node == self.tail:
#         # delete node
#         self.remove_from_tail()
#         # add node to head position
#         self.add_to_head(node)
#     else:
#         # save node to a new var
#         node_to_move = node
#         # delete the node
#         self.delete(node)
#         # add_to_head
#         self.add_to_head(node_to_move)