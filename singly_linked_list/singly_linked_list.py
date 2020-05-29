class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_head(self, value):
        current = self.head
        while current:
            yield current
            current = current.next


    def add_to_tail(self, value):
        new_node = Node(value, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    
    def contains(self, value):
        if value == self.value:
            return True
        else:
            return False 

    def remove_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
        
    def get_max(self):
        max_value = self.head.value
        current = self.head

        while current is not None:
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value