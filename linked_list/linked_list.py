"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""

### Linked Lists
# ? Should have the methods:
# * add_to_tail
# * remove_head
# * contains
# * get_max
# add_to_tail replaces the tail with a new value that is passed in.
# remove_head removes and returns the head node.
# contains should search through the linked list and return true if a matching value is found.
# get_max returns the maximum value in the linked list.
# The head property is a reference to the first node and the `tail` property is a reference to the last node. Build your nodes with objects.


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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head != None:
            old_head = self.head
            self.head = self.head.next_node
            return old_head.value
        else:
            return None

    def contains(self, i):
        if self.head == None:
            return False
        else:

            def search_list(node):
                if node.value == i:
                    return True
                elif node.next_node == None:
                    return False
                else:
                    return search_list(node.next_node)

            return search_list(self.head)

    def get_max(self):
        if self.head == None:
            return
        else:
            temp = 0

            def find_max(node, temp):
                if node == None:
                    return temp
                elif node.value > temp:
                    temp = node.value
                    return find_max(node.next_node, temp)
                else:
                    return find_max(node.next_node, temp)

            return find_max(self.head, temp)

    # def size(self):
    #     current = self.head
    #     count = 0
    #     while current:
    #         count += 1
    #         current = current.next_node
    #     return count
