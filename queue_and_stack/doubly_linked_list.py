"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    '''
    this object represents a single node in the linked list.
    it has a pointer to the next node and the previous node.
    '''
    def __init__(self, value, prev=None, next=None):
        # the value of the current node
        self.value = value
        
        # pointer to the node before it
        self.prev = prev

        # pointer to the node after it
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        # current_next is a self.next placeholder so we can overwrite the self.next variable to the next node
        # for example
        #   [1]<->[2]<->[3]<->[none]
        # we want to insert 4 after 2
        # since 2.next points to 3 we save that pointer as current_next
        # cur_nex = ->[3]
        # then we insert the new node [4] after 2
        # set prev = self, where self is the current node [2] (line 35)
        # and next = current_next, which points to 3
        # [1]<->[2]<->[4]<->[3]<->[None] 
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        # if current_next is None this wont be ran, meaning were at the tail
        # otherwise were still in the middle somewhere, in this case [3], so we set this nodes previous
        # pointer to the node that we just added. Which in this case is [4] 
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        # saves the node before the 'current' node 
        current_before_node = self.prev

        # creates a new node with the desired value (listnode)
        # the new node points (<-) to the node that came before
        # the new node points (->) to the node that comes before it
        # the current node points to the new node
        self.prev = ListNode(value, current_before_node, self)

        if current_before_node:
            current_before_node.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        # if the current nodes before node is not None ([1]<->[2]<->[3])
        # have the before node point to the node after the current node
        if self.prev:
            self.prev.next = self.next
        
        # if the current nodes after node is not None
        # have the after nodes previous node point to the current nodes previous node
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.head.insert_before(value)
            self.head = self.head.prev


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Planning
        # If LL is empty
        if not self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return
        # If node is head
        # If node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        
        # If node is in middle
        else:
            node.delete()

        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # Plan:

        # Max max var
        # Loop through nodes via node.next
        # If node.value is higher, update max
        # return max
        pass
