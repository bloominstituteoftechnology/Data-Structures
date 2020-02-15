import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

#FIFO

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __str__(self):
        cur_node = self.storage.head
        output = ''
        output += str(cur_node) + ' | '
        if self.storage.head == None and self.storage.tail == None:
            output = "Empty"
        else: 
            while cur_node.next is not None:
                cur_node = cur_node.next
                output += str(cur_node) + ' | '
        return output

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else: 
            return None

    def len(self):
        return self.size

test_q = Queue()

test_q.enqueue(1)
test_q.enqueue(2)
test_q.enqueue(3)

print(test_q)

test_q.dequeue()
test_q.dequeue()

print(test_q)

test_q.enqueue(2)
test_q.enqueue(1)

print(test_q)


