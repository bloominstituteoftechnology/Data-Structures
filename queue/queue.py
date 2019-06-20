class Node(object):
    def __init__(self, data=None, next_node="None"):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        new_node.set_next(self.tail)
        self.tail = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def remove_from_head():


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # Answer: Linked List
        self.storage = LinkedList()

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def len(self):
        return self.size
