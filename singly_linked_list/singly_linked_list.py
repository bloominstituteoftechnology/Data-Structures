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

    def __str__(self):
        return f"Head: {self.head} \nTail: {self.tail}"

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value)

        # Handle is self.tail is none
        if self.head is None and self.tail is None:
            # have both head and tail refer to the single node
            self.head = new_node
            # set new_node to be the tail
            self.tail = new_node
        else:
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

        return self.head.get_value()

    def remove_head(self):
        # if empty linked list
        if self.head is None and self.tail is None:
            return

        # if single elem in linked list
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()

        # if non empty
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if empty linked list
        if self.head is None and self.tail is None:
            # return nothing
            return

        # if non-empty linked list

        # start at head and iterate down
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        val = self.tail.get_value()

        # move self.tail to the Node right before
        self.tail = current
        return val


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_to_tail(10)
    ll.add_to_tail(3)
    ll.remove_tail()
    print(ll)
