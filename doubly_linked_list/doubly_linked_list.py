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

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.value) + '--->'
            itr = itr.next

        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.value) + '-->'
            itr = itr.prev
        print(llstr)

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        node = ListNode(value)

        # DLL is empty
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        # If head points to a node
        else:
            # new node.next points to the head node
            node.next = self.head
            # head.prev points to the new node
            self.head.prev = node
            # have the head pointing to the new node
            self.head = node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # value to remove
        removed_value = self.head.value

        # if head is not pointing to None
        if self.length > 1:
            # head points to the next node
            self.head = self.head.next
            # now that the head is point at the next node,
            # sever the connection from the old head by making it's next pointer point to None
            self.head.prev.next = None
            # new head.prev now points to None
            self.head.prev = None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            raise Exception('DLL is empty')

        self.length -= 1
        return removed_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        elif self.length == 1:
            self.tail = node
            self.tail.prev = self.head
            self.head.next = self.tail
        else:
            # capture where tail was previously
            cur = self.tail
            self.tail = node
            self.tail.prev = cur
            cur.next = self.tail

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        removed_value = self.tail.value

        if self.tail == self.head:
            self.tail = None
            self.head = None
        elif self.length == 2:
            self.head.next = None
            self.tail.prev = None
            self.tail = self.head
        elif self.length > 2:
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail.prev = None
            self.tail = new_tail

        self.length -= 1
        return removed_value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):

        itr = self.head
        while itr:
            if node == itr:
                # check if node == head
                if node == self.head:
                    self.remove_from_head()
                    break
                # check if node == tail
                elif node == self.tail:
                    self.remove_from_tail()
                    break
                else:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                    itr.next = None
                    itr.prev = None
                    self.length -= 1
                    break

            itr = itr.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):

        max_value = 0

        itr = self.head
        while itr:
            if itr.value > max_value:
                max_value = itr.value
            itr = itr.next

        return max_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):

        itr = self.head
        new_node = ListNode(node)

        while itr:
            if node == itr.value:
                if self.length <= 1:
                    return
                elif itr.next == None:
                    self.remove_from_tail()
                    self.add_to_head(new_node.value)
                else:
                    self.delete(node)
                    self.add_to_head(new_node.value)

            itr = itr.next

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):

        new_node = ListNode(node)
        itr = self.head

        while itr:
            # if no elements exist it won't go through this if
            if node == itr.value:
                # if 1 element exists, do nothing OR if the element is the tail, do nothing
                if self.length == 1 or itr.next == None:
                    return
                # if 2 elements exist, swap the two elements
                elif self.length == 2:
                    self.delete(itr)
                    self.add_to_head(new_node.value)
                else:
                    self.delete(itr)
                    self.add_to_tail(new_node.value)

            itr = itr.next


dll1 = DoublyLinkedList()
dll1.add_to_tail(1)
dll1.add_to_tail(2)
dll1.add_to_tail(3)
dll1.move_to_end(1)
dll1.print()
print(f'Head value: {dll1.head.value}')
print(f'Tail value: {dll1.tail.value}')

# dll1.add_to_tail(1)
# dll1.add_to_tail(2)
# dll1.add_to_tail(3)
# dll1.move_to_front(3)
# dll1.print()
# print(f'Head value: {dll1.head.value}')
# print(f'Tail value: {dll1.tail.value}')
