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
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value,self.head)
        self.head = new_node
        
        if self.length == 0:
            self.tail = new_node
        
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            
        else:
            self.tail.set_next(new_node)
            
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:

            return None
        
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1

            return value

        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1

            return value

    def remove_tail(self):

        if self.tail is None:

            return None
        
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1

            return value

        else:
            value = self.tail.get_value()
            element = self.head
            while element.get_next() != self.tail:
                element = element.get_next()
            self.tail = element
            self.tail.set_next(None)
            self.length -= 1

            return value

    def contains(self, value):
        to_return = False

        element = self.head
        while element is not None:
            to_return = True if (element.get_value() == value) else to_return
            element = element.get_next()

        return to_return

    def get_max(self):

        if self.length == 0:
            return None

        else:
            element = self.head
            max_val = self.head.get_value()
            while element is not None:
                max_val = element.get_value() if (element.get_value() > max_val) else max_val
                element = element.get_next()

            return max_val

