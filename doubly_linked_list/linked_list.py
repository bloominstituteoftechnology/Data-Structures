class Node:
    def __init__(self, value=None, next_node=None):
        # its own value
        self.value = value
        # the next node in the list
        self.next_node = next_node
    
    def get_value(self):
        # return the value of this node 
        return self.value

    def get_next(self):
        # return a reference to this node's next_node property
        return self.next_node

    def set_next(self, new_next):
        # set this node's `next_node` property 
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference the first node in the linked list
        self.head = None
        # reference to the last node in the linked list
        self.tail = None

    # add a new node to the tail of our list
    def add_to_tail(self, value):
        new_node = Node(value)
        # we have an empty linked list 
        # check the head reference 
        if self.head is None and self.tail is None:
            # both self.head and self.tail to point
            # to the new node we're adding
            self.head = new_node
            self.tail = new_node
        # every other case 
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    # remove and return the value of the head node 
    def remove_from_head(self):
        # make sure our list isn't empty
        if not self.head and not self.tail:
            return None
        # take another reference to the head we're
        # about to delete
        old_head_value = self.head.value
        # we only have a single node in the list 
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        # we have at least two nodes in the list 
        else:
            # move the self.head reference to refer
            # to the old head's next node 
            self.head = self.head.get_next()
            return old_head_value

    def contains(self, target):
        # make sure we don't have an empty list
        if not self.head and not self.tail:
            return False
        # init a current reference to refer to the current
        # node we're iterating on
        current = self.head
        # while the current node in the list is a valid Node
        while current:
            # check if the current node's value matches
            # what we're looking for 
            if current.value == target:
                return True
            # update the current reference to the next
            # node in the list
            current = current.get_next()
        # we've traversed the entire list
        return False

# class Node:
#     def _init_(self, next_node, value=None):
#         # its own value
#         self.value = value
#         # the next node in the list
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         # return a ref to this node's next_node's proerty
#         return self.next_node

#     def set_next(self, new_next):
#         # set this node's `next_node` property
#         self.next_node = new_next


# class LinkedList:
#     def _init_(self):
#         # ref the first node in linked_list
#         self.head = None
#         # ref the last node in linked list
#         self.tail = None

#     # add a new node to tail of our list
#     def add_to_tail(self, value):
#         new_node = Node(value)
#         if self.head and self.tail is None:
#             # we want both self.head and self.tail to
#             # point to the new node
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def remove_from_head(self, value):
#         # make sure list isn't empty
#         if self.head is self.tail:
#             # take another ref to the head we're about the delete
#             old_head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return old_head_value
#         # we have at least two nodes in list
#         else:
#             # take another ref to the head node
#             # we're about to delete it
#             old_head_value = self.head.value
#             # move the self.head ref to refer to the old head's next node
#             self.head = self.head.get_next()
#             return old_head_value

#     def contains(self, target):
#         # make sure we don't have an empty list
#         # cuz if its empty, it doesn't have what we are looking for
#         if not self.head and not self.tail:
#             return False
#         # init a current ref to refer to the current node we're iterating on
#         current = self.head
#         # whle the next node in the list is a valid node
#         while current.get_next():
#             # check if the current node's value matches what we are looking for
#             if current.value == target:
#                 return True
#             # update the current ref to the next node in the list
#             current = current.get_next()
#         # if we were not successful after traversing the whole thing
