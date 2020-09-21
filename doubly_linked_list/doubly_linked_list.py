"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
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
        node_values = []
        if self.head is None:
            return f"< >, len: {len(self)}"
        current_node = self.head
        node_values.append(current_node.value)
        while current_node.next is not None:
            current_node = current_node.next
            node_values.append(current_node.value)
        output = "< "
        output += ", ".join([str(node) for node in node_values])
        output += f" >, len: {len(self)}"
        return output
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        # wrap the input value in a node
        new_node = ListNode(value)
        # check if the linked list is empty
        if not self.head and not self.tail:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the head 
        else:
            # set the new node's `next` to refer to the current head
            new_node.next = self.head
            # set the current head's `prev` to refer to the new_node
            self.head.prev = new_node
            # set the list's head reference to the new node 
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        self.length -= 1
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        self.length -= 1
        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            return value
        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.length += 1
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        print(f"before: {self}")
        # zero nodes:
        if self.head is None:
            return
        # one node:
        if self.head is node and self.tail is node:
            self.length = 0
            self.head = None
            self.tail = None
        # 2+ nodes:
        else:
            self.length -= 1
            if node.prev:
                if node.next:
                    node.prev.next = node.next
                else:
                    node.prev.next = None
            else:
                self.head = node.next
            if node.next:
                if node.prev:
                    node.next.prev = node.prev
                else:
                    node.next.prev = None
            else:
                self.tail = node.prev
        print(f"after:  {self}")

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # start from head
        current_node = self.head
        # starting max_value
        max_value = current_node.value
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value