
# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.
# 3. What is the difference between using an array vs. a linked list when
#    implementing a Stack?
#
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value : Node):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def contains(self, value) -> bool:

        node = self.head

        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False

    def remove_head(self):

        if self.head is None:
            return
        else:
            value = self.head.value

            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next

            return value

    def get_max(self):
        max = None
        node = self.head

        while node is not None:
            if max is None:
                max = node.value
            elif node.value > max:
                max = node.value

            node = node.next

        return max


#
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        if self.storage.head is None:
            self.storage.head = Node(value)
            self.size += 1
        else:
            new_node = Node(value)
            new_node.next = self.storage.head
            self.storage.head = new_node
            self.size += 1

    def pop(self):

        if self.storage.head is None:
            return None

        else:
            self.size -= 1
            popped = self.storage.head.value
            self.storage.head = self.storage.head.next
            return popped




stack = Stack()
stack.push(100)
stack.push(101)
stack.push(105)

print(stack.pop())
print(stack.pop())
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#
#     def pop(self):
#
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()
#
# stack = Stack()
# stack.push(3)
# stack.push(4)
# stack.push(5)
# print(stack.storage)
# print(stack.pop())
