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

    def get_value(self):
        return self.value

    def __str__(self):
        return  

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
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set head to value wrapped in new node
            new_node.next = self.head  
            new_node.insert_before(value)
            self.head = new_node
        # increment length by one regardless 
        self.length += 1 
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # for empty LL
        if not self.head:
            return None 
        # self.tail is a Node so can call .prev on it
        # check if it's the end of the LL
        # elif (self.tail == self.head):
        elif self.head.prev == None: 
            value = self.head.get_value()
            self.tail = None 
            self.head = None 
            self.length -= 1
            return value 
        else:
            # need to return this so store first
            value = self.head.get_value()
            # remove it from the LL
            self.head.delete()
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail 
            new_node.insert_after(value)
            self.tail = new_node
        # increment length by one regardless 
        self.length += 1     

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # empty case
        if not self.tail:
            return None
        # single node case
        # elif (self.tail == self.head):
        # self.tail is a Node so can call .next on it
        # check if it's the end of the LL
        elif self.tail.next == None:
            value = self.tail.get_value()
            self.tail = None 
            self.head = None 
            self.length -= 1 
            return value 
        # else 
        else:
            value = self.tail.get_value()
            self.tail.delete()
            self.length -= 1 
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.add_to_head(node)
        node.value.delete()

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.add_to_tail(node)
        node.value.delete()

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest = 0
        while curr is not None:
            if curr > 0:
                highest = curr
        return highest

    def __str__(self):
        list_str = ''
        curr = self.head
        while curr is not None:
            flags = ''
            if curr is self.head:
                flags += '[H]'
            if curr is self.tail:
                flags += '[T]'
            list_str += f'{curr.prev} <-- {flags}{curr} --> {curr.next}\n'
            curr = curr.next
        return list_str