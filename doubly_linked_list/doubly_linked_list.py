"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def remove(self):
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
    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += '{} <=> '.format(current.value)
            current = current.next
        return output
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
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # if self.head == None and self.tail == None:
        #     return None
        # self.length -= 1
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # else:
            value = self.head.value
            self.delete(self.head)
            # self.head = self.head.next
            # self.head.prev = None
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
        # if self.head is None and self.tail is None:
        #     return None
        # self.length -= 1
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # else:
            value = self.tail.value
            self.delete(self.tail)
            # self.tail = self.tail.prev
            # self.tail.next = None
            return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return None
        if node is self.tail:
            self.delete(node)
            self.tail.prev = self.tail
        else:
            self.delete(node)
        value = node.value
        self.add_to_head(value)
        return value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return None
        else:
            self.delete(node)
        value = node.value
        '''following code is same as add_to_tail () '''
        # self.tail.next = node
        # node.prev = self.tail
        # node.next = None
        # self.tail = node
        self.add_to_tail(value)
        return value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
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
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            return value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self): 
        if self.head and self.tail:
            current = self.head.next
            maximum = self.head.value
            while current:
                if current.value > maximum:
                    maximum = current.value
                current = current.next
            return maximum

    def insert_item_after_index(self, value, index):
        node = ListNode(value)
        current = self.head
        counter = 1
        while current:
            if counter == index:
                if current.next:
                    temp = current.next
                    temp.prev = node
                    current.next = node
                    node.next = temp
                    node.prev = current
                else:
                    current = self.tail
                    self.tail = node
                    current.next = node
                    node.prev = current
            if self.length < index:
                print("Index is too high by {}".format(index-counter))
            counter += 1
            current = current.next

    def insert_item_before_index(self, value, index):
        node = ListNode(value)
        current = self.head
        counter = 1
        if self.length < index:
            print("Index is too high by {}".format(index-self.length))
        while current:
            if counter == index:
                if current.prev:
                    temp = current.prev
                    temp.next = node
                    current.prev = node
                    node.prev = temp
                    node.next = current
                else:
                    current = self.head
                    self.head = node
                    current.prev = node
                    node.next = current
            counter += 1
            current = current.next


dll = DoublyLinkedList()

dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.add_to_tail(10)
dll.add_to_tail(12)
dll.add_to_tail(15)
dll.add_to_head(11)
dll.add_to_head(22)
dll.add_to_head(33)
dll.add_to_tail(104)
dll.add_to_tail(1212)
dll.add_to_tail(15121)
dll.insert_item_before_index(290, 12)
dll.insert_item_after_index(1232, 1)
print(dll)
print(f'{dll.head.value} Initial head value')
print(f'{dll.tail.value} Initial tail value')
print(f"{dll.length} length")
print(f'Deleted item from head {dll.remove_from_head()}')
print(f'Deleted item from tail {dll.remove_from_tail()}')
print(f'Deleted item from any node {dll.delete(dll.head.next)}')
print(f'Moved item to the end {dll.move_to_end(dll.head)}')
print(f'Moved item to the front {dll.move_to_front(dll.tail)}')
print(f'{dll.length} length')
print(f'{dll.head.value} last head value')
print(f'{dll.tail.value} last tail value')
print(f'{dll.get_max()} max value')

