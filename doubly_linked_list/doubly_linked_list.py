"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    def __str__(self):
        return f'{self.value}'
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def get_value(self):
        return self.value
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
    def __str__(self):
        #return f'self.head is {self.head} \n self.tail is {self.tail} \n self.head.next is {self.head.next} \n self.head.prev is {self.head.prev} \n self.tail.next is {self.tail.next} \n self.tail.prev is {self.tail.prev}'
        '''print(current)
        current = current.next
        print(current)
        current = current.next
        print(current)'''
        current = self.head
        while current != None:
            print(current)
            current = current.next
        return 'Done'
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
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        old_head = self.head.get_value()
        new_head = self.head.next
        self.head.delete()
        if new_head == None:
            self.tail = None
            self.head = new_head
        else:
            self.head = new_head
        self.length -= 1
        return old_head
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #new_node = ListNode(value)
        if not self.head and not self.tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        old_tail = self.tail.get_value()
        new_tail = self.tail.prev
        self.tail.delete()
        if new_tail == None:
            self.head = None
        self.tail = new_tail
        self.length -= 1
        return old_tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if (node != None) and (node != self.head):
            if (node == self.tail) and (self.tail.prev != None):
                self.tail = self.tail.prev
            node.delete()
            old_head = self.head
            self.head.prev = node
            self.head = node
            node.next = old_head
            node.prev = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if (node != None) and (node != self.tail):
            if(node == self.head) and (self.head.next != None):
                self.head = self.head.next
            node.delete()
            old_tail = self.tail
            self.tail.next = node
            self.tail = node
            node.prev = old_tail
            node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node != None:
            if node == self.head:
                if node.next != None:
                    self.head = node.next
                    node.delete()
                    self.length -= 1
                else:
                    self.head= None
                    self.tail= None
                    node.delete()
                    self.length = 0
            elif node == self.tail:
                if node.prev != None:
                    self.tail= node.prev
                    node.delete()
                    self.length -= 1
                else: 
                    self.tail= None
                    self.head= None
                    node.delete()
                    self.length = 0
            else:
                node.delete()
                self.length -= 1
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        max_value = current.get_value()
        while current.next != None:
            if (current.get_value()) < (current.next.get_value()):
                max_value = current.next.get_value()
            current = current.next
        return max_value

'''test = DoublyLinkedList()
test.add_to_head(1)
test.add_to_tail(2)
test.add_to_tail(3)

test.move_to_end(test.head)

print(test)'''