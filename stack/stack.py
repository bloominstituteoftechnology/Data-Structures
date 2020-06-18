
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_list_size(self):
        acc = 0
        current_node = self.head
        while current_node is not None:
            acc += 1
            current_node = current_node.next_node
        return acc

    def delete_last_node(self):
        last_node = self.head

        while last_node.next_node is not None:
            prev_node = last_node
            # print('prev node:', prev_node.value)
            last_node = last_node.next_node
            # print('last node:', last_node.value)

        if self.head.next_node is None:
            self.head.next_node = None
            self.tail = None
            self.head = None
        elif self.head.next_node is not None:
            prev_node.next_node = None
            self.tail = prev_node


# mylist = LinkedList()
# mylist.add_to_head(1)
# mylist.add_to_head(7)
# mylist.add_to_head(3)
# mylist.add_to_head(4)
# mylist.add_to_head(99)
# # mylist.add_to_tail(2)
# mylist.delete_last_node()
# mylist.delete_last_node()
# print(mylist.head.value, mylist.tail.value)
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


# List Stack class ____________________________________________

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         length = len(self.storage)
#         self.size = length
#         return length

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()

# ________________________________________________________________

# NODE / LINKED LIST Stack class _________________________________

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.get_list_size()

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.get_list_size() > 0:
            return self.storage.delete_last_node()


# _______________________________________________________________
