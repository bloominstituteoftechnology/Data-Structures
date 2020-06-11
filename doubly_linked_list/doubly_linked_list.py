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

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        # Logic 1: There is already a head
        # Set old head as next for new_node
        # Set new_node a previous for old head
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        # Logic 2: There is no a head
        # Explictly declare new_node as tail 
        else:
            self.head = new_node
            self.tail = new_node

        

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
        new_node = ListNode(value)
        self.length += 1

        # Logic 1: There is already a tail
        # Set old tail as prev for new_node
        # Set new_node a next for old tail
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        # Logic 2: There is no tail
        # Explicitly declare new_node as head
        else:
            self.head = new_node
            self.tail = new_node

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
        # Logic 1: Node is already the head node
        if node is self.head:
            return
        # Logic 2: Node is not the head node
        self.add_to_head(node.value)
        self.delete(node)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Logic 1: Node is already the tail node
        if node is self.tail:
            return
        # Logic 2: Node is not the tail node
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Logic 1: Empty list
        if not self.head:
            print("Empty")
            return
        self.length -= 1

        # Logic 2: List size 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Logic 3: Node is head
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        # Logic 4: Node is tail
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        # Logic 5: All other cases
        else:
            node.delete()
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # Logic 1: Empty list
        if self.head == None:
            return "Empty list"
        # Logic 2: Head node = tail node
        elif self.head == self.tail:
            return self.head.value
        # Logic 3: All other cases
        else:
            self.node_values = []
            for items in range(self.length):
                self.number = self.head.next.value
                self.node_values.append(self.number)
            self.node_values.append(self.head.value)
            self.node_values.append(self.tail.value)
            return max(self.node_values)

