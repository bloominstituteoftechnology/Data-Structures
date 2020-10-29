"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

        # None <= 0 =>  <= 1 => <= 2 => <= None
        # 0 <= 1 => <= 2 => <= None
        # 1 <= 2 => <= None
        # 2 <= None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.head.prev = new_node
        self.head = new_node
        self.length += 1

        #[ 15 , 0, 1, 2, 3, 4, None]
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None

        value = self.head.value

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return value

        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

        #[None, 0, 1, 2, 3, 4, None]

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_node.prev = self.tail

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None

        value = self.tail.value

        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return value

        self.tail = self.tail.prev
        self.tail.next = None

        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if self.length > 1:
        #     # checks if the node is the current tail
        #     if self.tail == node:
        #         self.tail = node.prev
        #         self.tail.next = None
        #
        #         self.head.next = self.head
        #         self.head = node
        #         self.head.prev = None
        #
        #     else:
        #         self.head.next = self.head
        #         self.head.next.prev = node
        #         self.head = node
        #         self.head.prev = None
        if self.head == node:
            return

        if self.tail != node:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

            # [None, 1, 4, 0,  2, 3, None ]

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if self.length > 1:
        #     if self.head == node:
        #         self.head = node.next
        #         self.head.next = node
        #
        #         self.tail.prev = self.tail
        #         self.tail.prev.next = node
        #         self.tail = node
        #         self.tail.next = None
        #
        #     else:
        #         self.tail.prev = self.tail
        #         self.tail.prev.next = node
        #         self.tail = node
        #         self.tail.next = None
        if self.tail == node:
            return

        if self.head != node:
            node.prev.next = node.next
        else:
            self.head = node.next

        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return

        value = node.value

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value

        if node is self.head:
            self.head = node.next
            self.head.prev = None
            self.length -= 1
            return value

        elif node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            return value

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_val = self.head.value

        pointer = self.head
        # for(let i = 0; i < self.length; i++)

        while pointer is not None:
            if max_val < pointer.value:
                max_val = pointer.value

            pointer = self.head.next

        return max_val


