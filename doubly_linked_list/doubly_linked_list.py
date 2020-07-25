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
        # set this node's next_node reference to the passed in node
        self.next = new_next
            
    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        # set this node's next_node reference to the passed in node
        self.prev = new_prev

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

    def __str__(self):
        elements = []

        element = self.head
        while element is not None:
            elements.append(element.get_value())
            element = element.get_next()

        return str(elements)
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        
        new_node = ListNode(value=value, next=self.head)
        self.length += 1
        
        if self.head is None and self.tail is None:
            self.tail = new_node

        else:
            self.head.set_prev(new_node)

        self.head = new_node
            
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        
        if self.head is None:

            return None
        
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1

            return value

        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.head.prev = None
            self.length -= 1

            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        new_node = ListNode(value=value, prev=self.tail)
        self.length += 1
        
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)

        self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        
        if self.tail is None:

            return None
        
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.tail = None
            self.head = None
            self.length -= 1

            return value

        else:
            value = self.tail.get_value()
            self.tail = self.tail.get_prev()
            self.tail.next = None
            self.length -= 1

            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        self.add_to_head(node.value)
        self.delete(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        
        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        if self.head is None and self.tail is None:
            return None

        elif node.prev is None:
            self.remove_from_head()

        elif node.next is None:
            self.remove_from_tail()

        else:
            node.next.set_prev(node.prev)
            node.prev.set_next(node.next)

            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        if self.length == 0:
            return None

        else:
            element = self.head
            max_val = self.head.get_value()
            while element is not None:
                max_val = element.get_value() if (element.get_value() > max_val) else max_val
                element = element.get_next()

            return max_val