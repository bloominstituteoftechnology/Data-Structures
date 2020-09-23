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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            temp.prev = self.head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        temp = self.head
        if self.length == 0:
            temp = ListNode(None)
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.length -= 1
        return temp.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            self.tail = new_node
            self.tail.prev = temp
            temp.next = self.tail

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            temp = ListNode(None)
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
        self.length -= 1
        return temp.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        prev = node.prev
        if (node.next != None):
            next = node.next
            prev.next = next
            next.prev = prev

        temp = self.head
        self.head = node
        node.next = temp
        temp.prev = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0 or self.length == 1 or node == self.tail:
            return
        else:
            head = self.head
            tail = self.tail
            if node != head:
                tail.next = node
                node.prev = tail

                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev

            else:
                self.head = head.next
                tail.next = head
                tail.prev = None
                head.next = None
                head.prev = tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
