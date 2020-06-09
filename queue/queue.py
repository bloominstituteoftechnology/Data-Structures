"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class ArrQueue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage:  # If storage exists / is populated...
            return self.storage.pop(0)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.first = None  # No first
        self.last = None  # No last
        self.count = 0  # Set count to 0

    def __len__(self):
        return self.count  # Return the count

    def enqueue(self, value):
        if self.first is None:  # If first doesn't exist...
            node = Node(value)  # Set node to value
            self.first = node  # First entry is node
            self.last = node  # Also last entry is node
        else:  # Otherwise...
            node = Node(value)  # Set node to value
            self.last.next = node  # Set last to next.
            self.last = node  # Set node to the new last.
        self.count += 1  # add 1 to the count.

    def dequeue(self):
        if self.first is None:  # If first doesn't exist...
            return None  # Return none
        elif self.first.next is None:  # If the next doesn't exist...
            node = self.first  # Node is first
            self.first = None  # Redefining first as None
            self.last = None  # Redefinint last as None
            self.count -= 1  # Remove from the count
            return node.value  # Return node value.
        else:  # Otherwise, go to next.
            node = self.first
            self.first = self.first.next
            self.count -= 1
            return node.value

# 3. What is the difference between using an array vs. a linked list when
# implementing a Queue?

# The main difference between using an array and a linked list when
# implementing a queue was in complexity of enqueue / dequeue. Whereas arrays
# are more self-explanatory with append / pop, linked lists required more of
# what I almost want to call an interative approach of going through a 'chain'
