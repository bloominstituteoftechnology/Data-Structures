from singly_linked_list import Node, LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return self.storage.tail.get_value()

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_head()
