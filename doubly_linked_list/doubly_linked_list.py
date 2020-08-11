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

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

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
        # new_node = ListNode(value, self.prev, self.next)
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # new_node points to old self.head
            self.head.prev = new_node  # current node points back to new_node
            self.head = new_node  # head is now the new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
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
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        # return value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
        # return value
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        print(self.print_list())

        if self.head is None and self.tail is None:
            # print("No data to delete")
            return
        elif self.head == self.tail:
            # print('ONLY 1')
            self.length -= 1
            self.head = None
            self.tail = None
        elif self.head == node:
            # print('is head')
            self.length -= 1
            self.head = self.head.next
            node.delete()
        elif self.tail == node:
            # print('is tail')
            self.length -= 1
            self.tail = self.tail.prev
            node.delete()
        else:
            self.length -= 1
            node.next = node.prev
            node.prev = node.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        cur_node = self.head.next
        while cur_node:
            if cur_node.value > max_value:
                max_value = cur_node.value
            cur_node = cur_node.next
        return max_value

    def print_list(self):
        I = []
        cur = self.head
        while cur:
            I.append(cur.value)
            cur = cur.next
        return I