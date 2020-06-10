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


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if not self.head and not self.tail:
            self.head = ListNode(value)
            self.tail = self.head

        old_head = self.head
        old_head.insert_before(value)
        self.head = old_head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return None
        
        value = self.head.value
        self.head = self.head.next

        # if linked list had 1 node
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None

        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            old_tail = self.tail
            old_tail.insert_after(value)
            self.tail = old_tail.next

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head:
            return None
        
        value = self.tail.value
        self.tail = self.tail.prev

        # if linked list had 1 node
        if not self.tail:
            self.head = None
        else:
            self.tail.next = None

        self.length -= 1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.head is not node:
            node.prev.next = node.next

        if self.tail is not node:    
            node.next.prev = node.prev

        if self.head:
            node.prev = None
            node.next = self.head
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail is node:
            return

        if self.head is not node:
            node.prev.next = node.next

        if self.head:
            node.next.prev = node.prev

            if self.head is node:
                self.head = node.next

            if self.tail is node.next:
                node.next.next = node

            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

        return node
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head

        if current is None:
            return None
        elif current.next is None:
            return current.value
        else:
            max = current.value

            while current is not None:
                if max < current.value:
                    max = current.value
                current = current.next
        
            return max


   

    def print_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next