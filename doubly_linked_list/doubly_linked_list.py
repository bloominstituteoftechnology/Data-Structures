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


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    #def __str__(self, info):
    #    return f'{self.info}'

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        if not self.head and not self.tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            #this one is where I actually have to think
            current_head = self.head
            self.head = ListNode(value)
            self.next = current_head
            self.prev = None
            current_head.prev = self.head
            self.length +=1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        next_value = self.next
        if next_value is not None:
            self.length -= 1
            self.head = next_value
            self.prev = None
            self.next = next_value.next
        else:
            print('DLL is empty.')

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not self.head and not self.tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            current_tail = self.tail
            self.tail = ListNode(value)
            self.next = None
            self.prev = current_tail
            current_tail.prev = self.tail
            self.length +=1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        tail_value = self.prev
        if tail_value is not None:
            self.length -= 1
            self.tail = tail_value.prev
            self.prev = self.prev
            self.next = None
        else:
            print('DLL is empty.')

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node = ListNode(node)
        if self.head != node:
            print('headz', self.head)
            print('next', self.next)
            og_head = self.head
            node.next = None
            node.prev = None
            og_head.prev = node
            node.next = og_head
            self.next = self.next.next
            self.head = node
        else:
            print('This node is already the head.')
    #remove the node from linked list
    #set it as the head's previous node
    #set the node's next to be the head
    #set self.head to point to the moved node

    #what if the node is already the head?
    #what if the node is the tail?

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass


dll = DoublyLinkedList()
print(dll.length)
print('head:', dll.head)
print(' ')

dll.add_to_head(7)
print(dll.length)
print('head:', dll.head)
print(' ')

dll.add_to_head(10)
print(dll.length)
print('head:', dll.head)
print(' ')

dll.add_to_head(3)
print(dll.length)
print('head:', dll.head)
print(' ')

dll.remove_from_head()
print(dll.length)
print('head:', dll.head)
print(' ')

dll.add_to_head(22)
print(dll.length)
print('head:', dll.head)
print(' ')

dll.add_to_tail(53)
print(dll.length)
print('tail:', dll.tail)
print(' ')

dll.remove_from_tail()
print(dll.length)
print('tail:', dll.tail)
print(' ')

dll.move_to_front(53)
print(dll.length)
print('head:', dll.head)
print(' ')