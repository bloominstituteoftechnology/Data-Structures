from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self, head: Optional[Node] = None, tail: Optional[Node] = None):
        self.head = head
        self.tail = tail
    
    def insert_at_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node


    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def contains(self, value) -> bool:
            # Traverse through list, checking values
            node = self.head

            while node is not None:
                if node.value == value:
                    return True
                node = node.next

            return False
            
    def remove_head(self):
        # What if we have no nodes?
        # What if we only have one node?
        if self.head is None:
            return
        else :
            value = self.head.value

            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next
            
            return value
            
    def get_max(self):
        max = None
        node = self.head

        while node is not None:
            if max is None:
                max = node.value
            elif node.value > max:
                max = node.value

            node = node.next
        
        return max

