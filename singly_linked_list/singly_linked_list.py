class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        self.tail = None

    # we have access to the end of the list, we can directly add new nodes to it.
    # O(1) run time
    def add_to_end(self, value):
        # regardless whether the list is empty or not, wrap value in a Node
        new_node = Node(value)
        # what if the list is empty?
        if not self.head and not self.tail:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # what if the list is not empty?
        else:
            # set the current tail's next to the new node
            self.tail.set_next(new_node)
            # set self.tail to the new node
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # we already had access to the head, so no traversal needed.
    # O(1)
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head.
            value = self.head.get_value()
            # remove the value at the head.
            # update self.head
            self.head = self.head.get_next()
            return value

    # we don't have access to the end, so traversal is needed to get to the end of the list.
    # O(n)
    def remove_at_end(self):
        current = self.head
        # what if the list is empty?
        if not current:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current end.
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
        if previous is not None:
            self.tail = previous
            previous.next_node = None
        else:
            self.head = None
        value = current.get_value()

        return value