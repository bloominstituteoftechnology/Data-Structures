class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        pass


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to 
    the list's head and tail nodes.
    """
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        """ Returns length of Linked List """
        return self.length
    
    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        """
        current_head = self.head
        self.length += 1
        if self.head:
            self.head = ListNode(value, None, current_head)
            current_head.prev = self.head
        else:
            self.head = ListNode(value)
            self.tail = self.head
        
    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
        if self.head != None:
            current_head = self.head
            self.length -= 1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head.delete()
                self.head = current_head.next

            return current_head.value

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        """
        self.length += 1
        if self.tail:
            node = ListNode(value, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.tail = ListNode(value)
            self.head = self.tail
    
    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        tail = self.tail
        if self.tail != None:            
            self.length -=1
            if self.tail == self.head: 
                self.tail = None
                self.head = None
            else:
                self.tail = tail.prev
                self.tail.next = None
        return tail.value

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        """
        if self.head != None:
            current_head = self.head
            self.head = node
            self.head.next = current_head
            current_head.prev = self.head
        
    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        """
        if self.tail != None:
            self.remove_from_head()
            current_tail = self.tail
            self.tail = node
            current_tail.next = self.tail
            self.tail.prev = current_tail
            self.length += 1
        else:
            current_tail = self.tail
            self.tail = node
            current_tail.next = self.tail
            self.tail.prev = current_tail
            
    def delete(self, node):
        """
        Deletes the input node from the List, preserving the 
        order of the other elements of the List.
        """
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -=1

    def get_max(self):
        """
        Finds and returns the maximum value of all the nodes 
        in the List.
        """
        head = self.head
        maximum = self.head.value
        for i in range(1, self.length):
            head = head.next
            if head.value > maximum:
                maximum = head.value
        return maximum