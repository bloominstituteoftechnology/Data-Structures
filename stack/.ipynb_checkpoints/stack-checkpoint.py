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


class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []
        # self.storage = ?

    def __str__(self):
        return f"{self.stack}"

    def __len__(self):
        return f"Length of stack: {self.size}"

    def push(self, value):
        self.size += 1
        self.stack.append(value)

    def pop(self):
        self.size -= 1
        return self.stack.pop(-1)


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(1)
    a.pop()
    print(a)
    print(a.__len__())
