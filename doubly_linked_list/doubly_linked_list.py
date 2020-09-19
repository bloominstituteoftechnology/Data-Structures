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
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def __str__(self):
        return f"{self.value}"

            
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
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        if self.head is None and self.tail is None:

            new_node = ListNode(value)

            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node = ListNode(value)
            old_head = self.head
            old_head.set_prev(new_node)
            new_node.set_next(old_head)
            self.head = new_node
            self.length += 1
            #self.head.set_next(old_node)
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.head.set_prev(None)
            self.length -= 1
            return value
            


            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
            
        if self.head is None and self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node = ListNode(value)
            self.tail.set_next(new_node)
            old_tail = self.tail 
            self.tail = new_node
            self.tail.set_prev(old_tail)
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
      
        if self.head is None and self.tail is None:
            return None

        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.tail.get_value()
            new_tail = self.tail.get_prev()
            self.tail = new_tail
            self.tail.set_next(None)
            self.length -= 1
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            return None

        else:
            switched_node = node
            switched_node_prev_node = switched_node.get_prev()
            switched_node_next_node = switched_node.get_next()

            # switches node to head
            old_head = self.head
            old_head.set_prev(switched_node)
            switched_node.set_next(old_head)
            self.head = switched_node

            # redefines pointers
            if switched_node_next_node != None:
                switched_node_next_node.set_prev(switched_node_prev_node)
            else:
                self.tail = switched_node_prev_node
            if switched_node_prev_node != None:
                switched_node_prev_node.set_next(switched_node_next_node)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return None
        
        if self.head == self.tail:
            return None

        else:
            switched_node = node
            switched_node_prev_node = switched_node.get_prev()
            switched_node_next_node = switched_node.get_next()

            # moves node to tail 
            self.tail.set_next(switched_node)
            old_tail = self.tail
            self.tail = switched_node
            self.tail.set_prev(old_tail)
            self.tail.set_next(None)

            # moves pointers
            if switched_node_prev_node != None:
                switched_node_prev_node.set_next(switched_node_next_node)
            else:
                self.head = switched_node_next_node
            if switched_node_next_node != None:
                switched_node_next_node.set_prev(switched_node_prev_node)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        deleted_node = node
        deleted_node_prev_node = deleted_node.get_prev()
        deleted_node_next_node = deleted_node.get_next()


        if self.head == self.tail:
            deleted_node = None
            self.head = None
            self.tail = None
            self.length -= 1
            return
        if deleted_node_prev_node is None:
            deleted_node = None
            self.head = deleted_node_next_node
            self.length -= 1
            return
        if deleted_node_next_node is None:
            deleted_node = None
            self.tail = deleted_node_prev_node
            self.length -= 1
            return
        else:
            deleted_node = None
            deleted_node_prev_node.set_next(deleted_node_next_node)
            deleted_node_next_node.set_prev(deleted_node_prev_node)
            self.length -= 1
            return

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = 0
        curr_node = self.head

        while curr_node != None:
            if curr_node.get_value() > max:
                max = curr_node.get_value()
                print(max)
            curr_node = curr_node.get_next()
        return max
        
    def __str__(self):
        return f"head: {self.head}, tail: {self.tail}"


