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
        # create a node
        new_node = ListNode(value)

        # check if list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node

        # establish new relationships then reassign the head
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        
        if not self.head:
            return None
        
        self.length -= 1

        if not self.head.next:
            head = self.head.value
            self.head = None

            return head
        
        head = self.head.value
        self.head = self.head.next
        self.head.prev = None

        return head            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a node
        new_node = ListNode(value)

        # check if list is empty
        if not self.tail:
            self.head = new_node
            self.tail = new_node

        # establish new relationships then reassign the tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        
        self.length -= 1

        if not self.tail.prev:
            tail = self.tail.value
            self.tail = None
            return tail
        
        tail = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None

        return tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if empty
        if not self.head:
            raise NameError(f'Node "{node.value}" is not found: Empty List')

        # check for valid argument
        if not isinstance(node, ListNode):
            raise TypeError('Invalid Object Type. Expected: "ListNode"')

        # check if passed node is already the head
        if self.head == node:
            return 

        # placeholder
        current = self.head

        while current:
            if current == node:
                # remove refrences to current and have them point to each other
                next_node = current.next
                prev_node = current.prev
                next_node.prev = prev_node
                prev_node.next = next_node 

                add_to_head(node.value)
                head_updated = True
                break
        # If head not updated, raise error
        if not head_updated:
            raise NameError(f'Node "{node.value}" is not found in list')
                

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if empty
        if not self.tail:
            raise NameError(f'Node "{node.value}" is not found: Empty list')

        # check for valid argument
        if not isinstance(node, ListNode):
            raise TypeError('Invalid Object Type. Expected: "ListNode"')

        # check if passed node is already the head
        if self.tail == node:
            return

        # placeholder
        current = self.head

        while current:
            if current == node:
                # remove refrences to current and have them point to each other
                next_node = current.next
                prev_node = current.prev
                next_node.prev = prev_node
                prev_node.next = next_node 

                add_to_tail(node.value)
                tail_updated = True
                break
        # If tail not updated, raise error
        if not tail_updated:
            raise NameError(f'Node "{node.value}" is not found in list')

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if empty
        if not self.head:
            raise NameError(f'Node "{node.value}" is not found: Empty list')

        # check for valid argument
        if not isinstance(node, ListNode):
            raise TypeError('Invalid Object Type. Expected: "ListNode"')

        # placeholder
        current = self.head

        while current:
            if current == node:
                # remove refrences to current and have them point to each other
                next_node = current.next
                prev_node = current.prev
                next_node.prev = prev_node
                prev_node.next = next_node 

                current = None
                node_deleted = True
                break
        # if node not deleted rasie error
        if not node_deleted:
            raise NameError(f'Node "{node.value}" is not found in list')


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self): 
        # check for empty list     
        if not self.head:
            return None
        
        # set initial values
        max_val = 0
        current = self.head

        # iterrate through list
        while current:
            current_val = current.get_value()

            # compare values and update max when greater value presented
            if max_val < current_val:
                max_val = current_val

            current = current.get_next()

        return max_val