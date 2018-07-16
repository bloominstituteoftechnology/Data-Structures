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
        self.tail = Node(value)

    def remove_head(self):
        head = self.head
        self.head = None

        return head

    def contains(self, value):
        pass

    def get_max(self):
        pass


nodeA = Node('a') # current head
nodeB = Node('b')
nodeC = Node('c') # current tail

nodeA.next = nodeB
nodeB.next = nodeC

list = LinkedList()

list.head = nodeA
list.add_to_tail(nodeC)

print(list.head) # prints 'a'
print(list.tail.value) # prints '<__main__.Node object at 0x7f84ce7cba20>'

print(list.remove_head().value)