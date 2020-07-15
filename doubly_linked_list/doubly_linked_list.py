"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + " Next value: "+ str(self.next.value if self.next is not None else None) + " Previous Value: "+str(self.prev.value if self.prev is not None else None)
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
        if not isinstance(value, ListNode):
            node = ListNode(value, next=self.head)
        else:
            node = value
        if self.length > 0:
            self.head.prev = node
            node.next = self.head
        else:
            self.tail = node
        self.head = node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        removed_head = self.head
        if self.length > 1:
            self.head.next.prev = None
            self.head = self.head.next
        else: #This is the only node in the list.
            self.head = None
            self.tail = None
        self.length -= 1
        return removed_head.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if not isinstance(value, ListNode):
            node = ListNode(value, prev=self.tail)
        else:
            node = value
        if self.length > 0:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        removed_tail = self.tail
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.tail = None
            self.head = None
        self.length -= 1
        return removed_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        node.prev = None
        node.next = None
        self.add_to_head(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        node.prev = None
        node.next = None
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.prev is None and node.next is None: #List will be empty when this node is deleted.
            self.head = None
            self.tail = None
        elif node.prev is not None and node.next is None: #end of list
            node.prev.next = None
            self.tail = node.prev
        elif node.prev is None and node.next is not None: #Start of list
            node.next.prev = None
            self.head = node.next
        else: #Prev and Next are both not None, somewhere in the middle of the list
            node.next.prev = node.prev
            node.prev.next = node.next
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = 0
        while True:
            if current_node.value > max_value:
                max_value = current_node.value
            if current_node is self.tail:
                break
            current_node = current_node.next
        return max_value

    def print_linked_list(self): #Function for debugging purposes
        array = []
        current_node = self.head
        while True:
            if current_node is not None:
                array.append(current_node.value)
                current_node = current_node.next
                if current_node is self.tail:
                    array.append(current_node.value)
                    break
            else:
                break
        print(array)
