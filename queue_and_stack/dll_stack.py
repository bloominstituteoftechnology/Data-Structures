from doubly_linked_list import DoublyLinkedList
import sys


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #     because we will only ever need to pop or push from the tail of the list
        #     and we already have functions created to help us do this
        self.storage = DoublyLinkedList()

    def push(self, value):
        result = self.storage.add_to_tail(value)
        self.size = self.storage.length
        return result

    def pop(self):
        if self.size > 0:
            result = self.storage.remove_from_tail()
            self.size = self.storage.length
            return result
        else:
            return None

    def len(self):
        return self.storage.length


# Stack class tests
# s = Stack()
# print(s.len(), 0)
# s.push(2)
# print(s.len(), 1)
# s.push(4)
# print(s.len(), 2)
# s.push(6)
# s.push(8)
# s.push(10)
# s.push(12)
# s.push(14)
# s.push(16)
# s.push(18)
# print(s.len(), 9)

# print(s.pop(), 18)
# print(s.len(), 8)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# print(s.len(), 0)
