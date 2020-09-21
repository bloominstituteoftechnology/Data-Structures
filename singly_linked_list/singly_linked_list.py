class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

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

    def add_to_head(self, value):
        new_node= Node(value)
        # create Node from input
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            # if not empty
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        # if head has no next node
        if not self.head.get_next():
            head = self.head
            # have to change both head and tail since they are both the same item
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse this list
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        current = self.head
        # if there's nothing in the list
        if not current:
            return None
        # if there's only one thing in the list
        if not current.get_next():
            return current.get_value()
        max = current.get_value()
        # mistake: was only comparing the first element and it wasn't moving
        # "current" to the next element
        while current is not None:
            if max < current.get_value():
                max = current.get_value()
            current = current.get_next()
        return max

    def print_val(self):
        #val = self.head.value
        curr_node = self.head

        while curr_node is not None:
            print (f'##{curr_node.get_value()}\n')
            curr_node = curr_node.get_next()

