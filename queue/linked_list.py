class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
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

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def add_to_end(self, value):
        # reagardless of if the list is empty of not, we need to wrap the value
        # in a Node
        new_node = Node(value)
        # what if the lsit is empty?
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # We want to add the node to the last node on the list
            # we can get to the last nod eon th elist by traversing it
            self.tail.set_next(new_node)
            # we're at the end of the linked list
            self.tail = new_node

    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
        return value

    def print_ll_elements(self):
        current = self.add_to_head
        while current is not None:
            print(current.value)
            current = current.get_next()