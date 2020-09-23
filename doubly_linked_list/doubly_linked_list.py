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

    def next_node(self):
        if self.next:
            return self.next
        else:
            return None

    def prev_node(self):
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
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            # set the current head's prev node to the new node
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return "No head in List"
        else:
            self.length -= 1
            # get the old head into a ValueError
            removed_head = self.head.get_value()
            # get the next head
            new_head = self.head.next_node()
            # remove the current head
            self.head.delete()
            # set the current head's next as the new head
            self.head = new_head
            return removed_head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
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
        if not self.tail:
            return "No tail in List"
        else:
            self.length -= 1
            removed_tail = self.tail.get_value()
            new_tail = self.tail.prev_node()
            self.tail.delete()
            self.tail = new_tail
            return removed_tail
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        new_head_value = node.value
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_from_tail()
            self.add_to_head(new_head_value)
        else:
            self.delete(node)
            self.add_to_head(new_head_value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        new_tail_value = node.value
        if node == self.tail:
            return
        elif node == self.head:
            self.remove_from_head()
            self.add_to_tail(new_tail_value)
        else:
            self.delete(node)
            self.add_to_tail(new_tail_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.length -= 1
            node.delete()
            self.head = None
            self.tail = None
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
          self.length -= 1
          node.delete()

    def get_all_nodes(self):
        if not self.head and not self.tail:
            print("No nodes in List")  
        else:
            current_node = self.head
            while current_node:
                print(f"{current_node.value.value}")
                current_node = current_node.next_node()
            print(self.tail.get_value().value)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.next_node()
        return max_value
