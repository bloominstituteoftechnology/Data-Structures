# Node
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# Singly list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# add_to_head performance:
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            # set the new node as the tail if the list is currently empty
            self.tail = new_node

# add_to_tail performance:
    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            # set the new node as the head if the list is currently empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

# remove_head performance:
    def remove_head(self):
        if not self.head:
            # the list is already empty
            return None

        removed_value = self.head.get_value()
        self.head = self.head.next
        if not self.head:
            # the list is now empty as the one and only item was removed
                self.tail = None
        return removed_value

# remove tail performance:
    def remove_tail(self):
        if not self.head:
            # the list is already empty
            return None

        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()

        prev.set_next(None)
        self.tail = prev
        return curr

# get_max performance:
    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            curr = curr.get_next()
        return max_value

# contains performance:
    def contains(self, value):
        curr = self.head
        while curr != None:
            if curr.get_value() is value:
                return True
            curr = curr.get_next()
        return False