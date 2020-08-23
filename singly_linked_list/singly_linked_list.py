# Implement Node Class

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
    
#     def set_next_node(self, next):
#         self.next = next

#     def get_next_node(self):
#         return self.next

#     def get_value(self):
#         return self.value

# Implement Linked List

# class LinkedList:
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_next_node(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        node = Node(value, None)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        

    def contains(self, value):
        if not self.head:
            return False

        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True

            current_node = current_node.get_next_node()
        return False

    def remove_head(self):
        if not self.head:
            return None
        
        if not self.head.get_next_node():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        head_value = self.head.get_value()
        self.head = self.head.get_next_node()
        return head_value



    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value

        current_node = self.head
        while current_node.get_next_node() is not self.tail:
            current_node = current_node.get__next_node()

        value = self.tail.get_value()
        self.tail = current_node
        return value
    
    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()
        current_node = self.head.get_next_node()

        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
        return max_value