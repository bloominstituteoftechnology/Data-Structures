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
        if self.next:
            return self.next
        else:
            return None

    def get_previous(self):
        if self.prev:
            return self.prev
        else:
            return None
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.value = None
        self.next = None
        self.prev = None
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
        root = ListNode(value)
        if self.head and self.tail:
            root.next = self.head
            self.head.prev = root
            self.head = root
        else:
            self.head = root
            self.tail = root
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        headValue = self.head.get_value()
        newHead = self.head.get_next()
        self.delete(self.head)
        self.head = newHead
        self.length -= 1
        return headValue
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        endNode = ListNode(value)
        if self.head and self.tail:
            endNode.prev = self.tail
            self.tail.next = endNode
            self.tail = endNode
        else:
            self.head = endNode
            self.tail = endNode
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tailValue = self.tail.get_value()
        newTail = self.tail.get_previous()
        self.delete(self.tail)
        self.tail = newTail
        self.length -= 1
        return tailValue

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_from_tail()
            self.add_to_head(value)
        else:    
            nextNode = node.get_next()
            previousNode = node.get_previous()
            previousNode.next = nextNode
            nextNode.prev = previousNode
            self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        if node == self.tail:
            return
        elif node == self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            nextNode = node.get_next()
            previousNode = node.get_previous()
            previousNode.next = nextNode
            nextNode.prev = previousNode
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.get_next()
            node.delete()
        elif self.tail == node:
            self.tail == node.get_previous()
            node.delete()
        else:
            node.delete()
        self.length += 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.get_next()

        return max_value
