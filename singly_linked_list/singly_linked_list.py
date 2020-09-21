#Node
class Node:
    def __init__(self, value=None, next_value=None):
        self.value= value
        self.next_value = next_value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_value

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next_value = new_next

#Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
            
    def remove_head(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

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

        # contains performance: O(n)
    def contains(self, value):
        curr = self.head
        while curr != None:
            if curr.get_value() is value:
                return True
            curr = curr.get_next()
        return False
