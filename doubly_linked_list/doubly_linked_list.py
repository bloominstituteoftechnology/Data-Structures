"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
      

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        current = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            current.prev = new_node
            self.head = new_node
        

    def remove_from_head(self):
        self.length -= 1
        current = self.head
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
            return current.value
        else:
            self.head = None
            self.tail = None
            return current.value
            

    def add_to_tail(self, value):
        self.length += 1 
        new_node = ListNode(value, self.tail)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        

    def remove_from_tail(self):
        self.length -= 1
        current = self.tail
        if self.tail.prev is not None:
            self.head.next.prev = None
            self.head = self.head.next
            return current.value
        else:
            self.head = None
            self.tail = None
            return current.value
            
    def move_to_front(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else: 
            self.tail = node.prev
        self.length -= 1
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        else: 
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        self.length -= 1
        self.add_to_tail(node.value)

    def delete(self, node):
        self.length -= 1   
        if node.prev:
            node.prev.nex = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def get_max(self):
        # If empty
        if not self.head:
            return None
        highest = self.head.value
        current = self.head.next
        while current:
            if current.value > highest:
                highest = current.value
            current = current.next
        return highest
