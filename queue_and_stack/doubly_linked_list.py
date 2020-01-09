"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # """Wrap the given value in a ListNode and insert it
    # after this node. Note that this node could already
    # have a next node it is point to."""
    # def insert_after(self, value):
    #     current_next = self.next
    #     self.next = ListNode(value, self, current_next)
    #     if current_next:
    #         current_next.prev = self.next

    # """Wrap the given value in a ListNode and insert it
    # before this node. Note that this node could already
    # have a previous node it is point to."""
    # def insert_before(self, value):
    #     current_prev = self.prev
    #     self.prev = ListNode(value, current_prev, self)
    #     if current_prev:
    #         current_prev.next = self.prev

    # """Rearranges this ListNode's previous and next pointers
    # accordingly, effectively deleting this ListNode."""
    # def delete(self):
    #     if self.prev:
    #         self.prev.next = self.next
    #     if self.next:
    #         self.next.prev = self.prev
    
    def __str__(self):
        return str(self.value)


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        cur_node = self.head
        output = ''
        output += str(cur_node) + ' | '
        if self.head == None and self.tail == None:
            output = "Empty"
        else: 
            while cur_node.next is not None:
                cur_node = cur_node.next
                output += str(cur_node) + ' | '
        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head

            self.head = new_node

            old_head.prev = self.head
            self.head.next = old_head
        
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        old_head = self.head

        if self.head is None:
            print("Empty")

        elif self.length == 1:
            self.head = None
            self.tail = None
        else: 
            new_head = old_head.next

            self.head = new_head
            old_head.next = None
            self.head.prev = None
        
        self.length -= 1

        return old_head.value
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail

            self.tail = new_node

            old_tail.next = self.tail
            self.tail.prev = old_tail

        self.length += 1
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        old_tail = self.tail

        if self.tail is None:
            print("Empty")
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_tail = old_tail.prev

            self.tail = new_tail

            new_tail.next = None
        self.length -= 1

        return old_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = None
        current_node = self.head
        old_head = self.head

        while current_node is not None:
            if current_node.value == node:
                value = current_node
                break
            
            current_node = current_node.next
        
        if value is self.head:
            return print("Value at front")

        if value is self.tail:
           self.tail = value.prev
           value.prev.next = None

           self.head = value
           self.head.prev = None
           self.head.next = old_head
           old_head.prev = self.head
               
        elif value is not self.tail:
            old_value = value
            old_value.prev.next = old_value.next
            old_value.next.prev = old_value.prev

            value.next = None
            value.prev = None

            self.head = value
            self.head.prev = None
            self.head.next = old_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass

dll = DoublyLinkedList()

dll.add_to_tail(1)
dll.add_to_tail(2)
dll.add_to_tail(3)

print(dll)

dll.remove_from_tail()
dll.remove_from_tail()
dll.remove_from_tail()

print(dll)
