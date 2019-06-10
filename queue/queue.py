from linked_list import LinkedList

# Array solution


class Queue2:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        if len(self.storage) < 1:
            return None
        return self.storage.pop(0)

    def len(self):
        return len(self.storage)

# Linked List solution


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size = self.size + 1

    def dequeue(self):
        if self.size is not 0:
            deleted_head = self.storage.remove_head()
            self.size = self.size - 1
            return deleted_head

    def len(self):
        return self.size
