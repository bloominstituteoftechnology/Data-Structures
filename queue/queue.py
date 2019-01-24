from linked_list import LinkedList
import sys
sys.path.append('../linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        value = self.storage.head.value
        self.storage.remove_head()
        return value

    def len(self):
        curr_node = self.storage.head
        iterations = 0
        while True:
            if curr_node is None:
                return iterations
            else:
                curr_node = curr_node.next_node
                iterations += 1
