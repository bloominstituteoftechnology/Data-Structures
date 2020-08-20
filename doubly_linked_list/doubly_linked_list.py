"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    
    def set_prev(self, new_prev):
        self.prev = new_prev
    
    def set_next(self, new_next):
        self.next = new_next

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

    def empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.empty():
            return None
        
        prev_head = self.head

        if prev_head.get_next() is None:
            self.head = None
            self.tail = None
        else:
            self.head = prev_head.get_next()
            self.head.prev = None
        self.length -= 1

        return prev_head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.empty():
            return None
        
        prev_tail = self.tail

        if prev_tail.get_prev() is None:
            self.head = None
            self.tail = None
        else:
            self.tail = prev_tail.get_prev()
            self.head.next = None
        self.length -= 1

        return prev_tail.get_value()
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.empty():
            return
        cur_node = self.head

        while cur_node is not None:
            if cur_node == node:
                if cur_node.prev is not None:
                    cur_node.prev.next = cur_node.get_next()
                if cur_node.next is not None:
                    cur_node.next.prev = cur_node.get_prev()

                cur_node.next = self.head
                cur_node.prev = None
                self.head = cur_node
                return
            else:
                cur_node = cur_node.get_next()
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.empty():
            return
        cur_node = self.head

        while cur_node is not None:
            if cur_node is node:
                if cur_node.prev is not None:
                    cur_node.prev.next = cur_node.get_next()
                if cur_node.next is not None:
                    cur_node.next.prev = cur_node.get_prev()

                if cur_node is self.head:
                    self.head = cur_node.get_next()
                    self.head.prev = None

                cur_node.next = None
                cur_node.prev = self.tail
                self.tail = cur_node

                if self.head.get_next() is None:
                    self.head.next = self.tail
                return
            else:
                cur_node = cur_node.get_next()


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.empty():
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        cur_node = self.head

        while cur_node is not None:
            if cur_node is node:
                if cur_node.prev is not None:
                    cur_node.prev.next = cur_node.get_next()
                if cur_node.next is not None:
                    cur_node.next.prev = cur_node.get_prev()
                if cur_node is self.head:
                    self.head = cur_node.get_next()
                    self.head.prev = None
                if cur_node is self.tail:
                    self.tail = cur_node.get_prev()
                    self.tail.next = None
                cur_node = None
            else:
                cur_node.get_next()
        self.length -= 1
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        
        cur_node = self.head
        max_val = cur_node.get_value()

        while cur_node is not None:
            max_val = max(max_val, cur_node.get_value())
            cur_node = cur_node.get_next()        
        return max_val