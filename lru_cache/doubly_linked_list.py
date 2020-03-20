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

    def __len__(self):
        return self.length
    def __str__(self):
        if self.head is None and self.tail is None: 
            return "empty"
        curr_node = self.head
        output = ''
        output += f'( {curr_node.value} ) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next 
            output += f'( {curr_node.value} ) <-> '
        return output


    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node

    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value


    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    def move_to_front(self, node):
        if node is self.head:
            return
        node_value = node.value
        #delete the node
        self.delet(node)
        self.add_to_head(node_vale)
        

    def move_to_end(self, node):
        if node is self.head:
            return
        node_value = node.value
        #delete the node
        self.delet(node)
        self.add_to_head(node_vale)

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return

    def get_max(self):
        pass
