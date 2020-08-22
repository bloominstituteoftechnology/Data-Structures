
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        newNode = Node(value, None)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            oldTail = self.tail
            oldTail.next = newNode
            self.tail = newNode

    def remove_head(self):
        if self.head is None:
            return None
        else:
            if self.head == self.tail:
                oldHead = self.head
                self.head = None
                self.tail = None
                return oldHead.value
            else:
                currentHead = self.head
                self.head = currentHead.next
                return currentHead.value

    def remove_tail(self):
        if self.head == None:
            return None

        elif self.head == self.tail:
            oldTail = self.tail
            self.head = None
            self.tail = None
            return oldTail.value

        else:
            current = self.head
            oldTail = self.tail
            while current.next is not self.tail:
                current = current.next

            removedValue = self.tail.value
            self.tail = None
            self.tail = current
            return removedValue