# from singly_linked_list import LinkedList
#!/usr/bin/env python3
import os
import sys
sys.path.append(f'{os.getcwd()}/singly_linked_list')
from singly_linked_list import LinkedList, Node


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


class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        count = 0
        curr = self.head
        if not curr:
            return count
        while curr.next:
            count += 1
            curr = curr.next
        return count + 1

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            head = self.head
            self.head = new_node
            self.head.next = head

    def pop(self):
        head = self.head
        if not self.head:
            return None
        else:
            head = self.head
            self.head = head.next
            return head.value


stack = Stack()
stack.push(101)
stack.push(102)
stack.push(105)
stack.print_list()
print(len(stack))
stack.pop()
stack.print_list()
