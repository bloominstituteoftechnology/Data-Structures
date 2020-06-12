class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
            self.tail = new_node

    def make_new_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        previous_head = self.head
        self.head = new_node
        self.head.set_next(previous_head)

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_from_tail(self):
        if not self.head:
            return None
        else:
            previous = self.head
            current = self.head
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            self.tail = previous
            previous.set_next(None)
            return current

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()
    
    def reverse(self, current, previous):
        self.tail = self.head
        if current.get_next() is None:
            self.head = current
            current.next_node = previous
            return
        reverse_next = current.get_next()
        current.next_node = previous
        self.reverse(reverse_next, current)




ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)
ll.add_to_tail(5)
ll.add_to_tail(7)



ll.print_list()
print(f"LL Head: {ll.head.value}")
print(f"LL Tail: {ll.tail.value}")
print("Seperator")
ll.reverse(ll.head, None)
ll.print_list()
print(f"LL Head: {ll.head.value}")
print(f"LL Tail: {ll.tail.value}")
print("Seperator")
ll.reverse(ll.head, None)
ll.print_list()
print(f"LL Head: {ll.head.value}")
print(f"LL Tail: {ll.tail.value}")
print("Seperator")