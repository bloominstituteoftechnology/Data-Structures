class Node():                                                              #<<<
    def __init__(self, value, next=None):
        self._value = value
        self._next_node = next
    
    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_node

    def set_next(self, new_next):
        self._next_node = new_next

    @property
    def value(self):
        return self._value
    @property
    def next_node(self):
        return self._next_node

    @value.setter
    def value(self, x):
        self._head = x
    @next_node.setter
    def next_node(self, x):
        self._next_node = x


class singleLinkedList():                                                  #<<<
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head
    @property
    def tail(self):
        return self._tail

    @head.setter
    def value(self, x):
        self._head = x
    @tail.setter
    def left(self, x):
        self._tail = x

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def remove_tail(self):
        if self._tail is None:
            return None
        data = self._tail.get_value()
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.get_next() != self._tail:
                current = current.get_next()
            self._tail = current
        return data

    def remove_head(self):
        if self._head is None:
            return None
        data = self._head.get_value()
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.get_next()
        return data

    def contains(self, data):
        if not self._head:
            return False
        current = self._head 
        while current is not None:
            if current.get_value() == data:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self._head is None:
            return None
        max_so_far = self._head.get_value()
        current = self._head.get_next()
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()
            current = current.get_next()
        return max_so_far


if __name__ == "__main__" and __package__ is None:
    pass