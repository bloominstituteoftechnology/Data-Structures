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
        current_head = self.head
        if self.head:  #if head exists
            self.head = ListNode(value, None, current_head)
            current_head.prev = self.head
        else: #If head doesn't exist, that means there's no tail either. So we assign the new node to head AND tail
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
        # return self.head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head: #if head actually exists...
        
            current_head = self.head
            if self.head == self.tail: #if there is only one node, make both head and tail none
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head.delete()
                self.head = current_head.next
                self.length -= 1
                
            return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail: #if tail exists
            newNode = ListNode(value, self.tail)
            self.tail.next = newNode
            self.tail = newNode
        else: #Tail doesn't exist means head doesn't exist either
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        if self.tail:
            self.length -= 1
            if self.tail == self.head: #could also be self.length == 1
                # current_tail = self.tail
                self.tail = None
                self.head = None
        
            else:
                # current_tail = self.tail
                self.tail = current_tail.prev
                self.tail.next = None

        
        if current_tail:

            return current_tail.value
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node == self.tail and node.prev:
            self.tail = node.prev
            self.tail.next = None
        if self.head:
            node.delete()
            current_head = self.head
            self.head = node
            self.head.next = current_head
            current_head.prev = self.head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.tail:
            if node == self.head:
                self.remove_from_head()
                current_tail = self.tail
                self.tail = node
                current_tail.next = self.tail
                self.tail.prev = current_tail
                self.length +=1
            else:

                current_tail = self.tail
                node.delete()
                self.tail = node
                current_tail.next = self.tail
                self.tail.prev = current_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        for i in range(1,self.length):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value