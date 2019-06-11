"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
          current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
          current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
          self.prev.next = self.next
        if self.next:
          self.next.prev = self.prev
          
    #  Returns next ListNode
    def get_next(self):
        return self.next

    #  Sets next ListNode to 'node' argument
    def set_next(self, next):
        self.next = next
        
    #  Returns next ListNode
    def get_prev(self):
        return self.prev

    #  Sets next ListNode to 'node' argument
    def set_prev(self, prev):
        self.prev = prev
 
    #  Sets next ListNode to 'node' argument
    def get_value(self, prev):
        return self.value      
        

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            return
        new_node = ListNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def remove_from_head(self):
        pass

    def add_to_tail(self, value):
        if not self.tail:
            new_node = ListNode(value)
            self.tail = new_node
            return
        while self.tail.next is False:
            new_node = ListNode(value)
            self.tail.next = new_node
            new_node.prev = self.tail.next
        self.length += 1
        
    def remove_from_tail(self):
        if self.tail is None:
            return "This list has no item to delete"
        if self.tail.next is None:
            self.tail = None
            return
        while self.tail.next is not None:
            self.tail.next.prev.next = None

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass
      
    def get_max(self):
        pass
