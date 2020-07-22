class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_tail(self, value):
        # 1. Create the Node from the value
        new_node = Node(value)
        # So, what do we have to do if tail is None?
        # What's the rule we want to set to indicate that the linked list is empty?
        # Would it be better to check the head?
        # let's check them both: an empty linked list has an empty head and an empty tail
        if self.head is None or self.tail is None:
            # in a one-element linked list, what should head and tail be referring to?
            # have both the head and the tail referring to the single node
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
            self.count = 1
        else:
            # These three steps assume that the tail is already referring to a Node
            # 2. Set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. Reassign self.tail to refer to the new Node
            self.tail = new_node
            self.count += 1

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the Same Node
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # self.head to the Node after the head
        self.head = self.head.get_next()
        self.count -= 1
        return val

    def remove_tail(self):
        # if we have a non-empty linked list
        if self.head is None and self.tail is None:
            return
        # move self.tail to the Node right before
        # we have to start at the head and move down the linked list
        # until we get to the node right before the tail
        # iterate over our linked list
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, `current` is the node right before the tail
        # set the tail to be None
        val = self.tail.get_value()
        self.tail = None
        self.count -= 1
        # move self.tail to the Node right before
        self.tail = current
        return val

    def contains(self, item):
        if self.head == None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == item:
                    return True
                current = current.get_next()
            return False

    def get_max(self):

        if self.head == None:
            return
        else:
            current = self.head
            max = 0

            while current is not None:
                if current.value > max:
                    max = current.value
                else:
                    current = current.get_next()
            return max







ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)
