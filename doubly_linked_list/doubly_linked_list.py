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
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        self.length -= 1
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            value = self.head.value
            next_head = self.head.next
            self.head = next_head
            next_head.prev = None
            return value
    # Point head to next node
    # Get rid of the prev of new head and point it to None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head and self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
            
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
            self.head = None
            self.tail = None
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            return value
       
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
        
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
        # if self.head is None and self.tail is None:
        #     return None
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.head == node:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            return value
        if self.tail == node:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return value
        else:
            value = node.value
            node.prev.next = node.next
            node.next.prev = node.prev
            return value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass



dll = DoublyLinkedList()

dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.add_to_tail(10)
print(f'{dll.head.value} head value')
print(f"{dll.length} length") 
# print(f'Deleted item {dll.remove_from_head()}')
# print(f'Deleted item {dll.remove_from_tail()}')
print(f'Deleted item {dll.delete(dll.tail.prev)}')
print(f'{dll.length} length')
print(f'{dll.head.value} head value')
print(f'{dll.tail.value} tail value')




