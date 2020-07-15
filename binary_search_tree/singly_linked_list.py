# List Item Node
# Has a value, a next
# get_value, set_value, get_next, set_next

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'[List Node: Value={self.value}]'

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

# Linked List
# Has a head, a tail
# get_head, set_to_head, get_tail, set_to_tail, remove_head, remove_tail, reverse 

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def __str__(self):
        return f'Linked List: Head={self.head}, Tail={self.tail}'

    def get_head(self):
        return self.head
    
    def add_to_head(self, value):
        node = ListNode(value, None)
        if self.head:
            node.set_next(self.head)
            self.head = node
        else:
            self.head = node
            self.tail = node

    def remove_head(self):
        if not self.head:
            return
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def get_tail(self):
        return self.tail
    
    def add_to_tail(self, value):
        node = ListNode(value, None)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_tail(self):
        if not self.tail:
            return
        if self.head.next == None:
            self.head = None
        current = self.head.next
        while current.next.next:
            current = current.next
        self.tail = current

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_max(self):
        if not self.head:
            return
        max_value = self.head.get_value()
        current_node = self.head.get_next()
        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.get_next()
        return max_value