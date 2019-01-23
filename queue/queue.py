import sys
sys.path.append('../linked_list')

from linked_list import LinkedList  # noqa


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        # add_to_tail from linkedlist
        self.storage.add_to_tail(item)
        # add one to self.size
        self.size = self.size + 1
        pass

    def dequeue(self):
        if self.size is not 0:
            # remove head from linked list
            deleted_value = self.storage.remove_head()
            # subtract 1 from size
            self.size = self.size - 1
            return deleted_value

            pass

    def len(self):
        return self.size
        pass