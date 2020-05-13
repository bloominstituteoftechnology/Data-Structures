class Node:
    def __init__(self, value=None, next_node=None):
        # val at this linked list node

        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# li = Node(1)
# li.set_next(Node(2))
# li.next_node.next_node = Node(3)
# li.next_node.next_node.next_node = Node(4)

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None

    def add_to_end(self, value):
        # regardless of if the list is empy or not, we need to wrap the value in a Node

        # value is actual value, and hasnt been wrapped in a node yet

        new_node = Node(value)
        # what if the list is empty?
        if not self.head:  # this is a way to write empty arrays
            self.head = new_node
        # what if the list isnt empty
        else:
            # self.head.set_next(new_node)

            # what node do we want to add the new node to?
            # The last node in the list
            # HOW: We can get to the last node in the list by traversing it
            current = self.head  # name the reference (current) and update i
            while current.get_next() is not None:
                current = current.get_next()  # keep going
            # we are a the end of the linked list
            current.set_next(new_node)

        def remove_from_head(self):
            # what if the list is empty?
            if not self.head:
                return None
            # what if it isnt empty?
            else:
                # we want to return the value at the current head
                value = self.head.get_value()  # want to over write the head

                # we want to remove the value at the head
                # update self head ---> it nees to refer the next element next in line
                self.head = self.head.get_next()
                return value

# li = Node(1)
# li_2 = Node(2)
# li_3 = Node(3)
# li_4 = Node(4)
# li.set_next(li_2)
# li_2.set_next(li_3)
# li_3.set_next(li_4)
