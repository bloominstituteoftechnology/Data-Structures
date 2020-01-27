from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.list = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.list.add_to_head(value)

    def pop(self):
        # if self.size < 1:
        #     return
        self.size -= 1
        self.list.remove_from_head()

    def len(self):
        return self.size


List1 = Stack()

List1.push(1)
List1.push(2)

List1.pop()
print(List1.len())
