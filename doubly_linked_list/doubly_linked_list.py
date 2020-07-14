
class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # def add_to_head(self, value):
    #     """
    #     Wraps the given value in a ListNode and inserts it
    #     as the new head of the list. Don't forget to handle
    #     the old head node's previous pointer accordingly.
    #     """
    #     if self.length == 0:
    #         new_node = ListNode(value)
    #         self.head = new_node
    #         self.tail = new_node
    #         self.length += 1
    #     else:
    #         current_node = self.head
    #         new_node = ListNode(value)
    #         current_node.prev = new_node
    #         self.head = new_node
    #         self.head.next = current_node
    #         print("Current head value:", current_node.value)
    #         self.length += 1

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # IF list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        """
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """
        if self.length == 0:
            return None
        else:
            if not self.head.next:
                current_node = self.head
                self.head = None
                self.tail = None
                self.length -= 1
                return current_node.value
            else:
                current_node = self.head
                new_head = current_node.next
                # Remove reference to old head from new head
                new_head.prev = None
                # Redefine new head as head node
                self.head = new_head
                self.length -= 1
                return current_node.value

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly.
        """
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node = self.tail
            new_node = ListNode(value, prev=current_node)
            current_node.next = new_node
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        if self.length == 0:
            return None
        else:
            if not self.tail.prev:
                current_node = self.tail
                self.head = None
                self.tail = None
                self.length -= 1
                return current_node.value
            else:
                current_node = self.tail
                new_tail = current_node.prev
                # Remove reference to old head from new head
                new_tail.next = None
                # Redefine new head as head node
                self.tail = new_tail
                self.length -= 1
                return current_node.value

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new head node of the List.
        """
        if node is self.head:
            return None
        else:
            if node is self.tail and self.length == 2:
                old_head = self.head
                self.tail = old_head
                self.head = node
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                value = node.value
                old_head = self.head
                self.delete(node)
                self.add_to_head(value)
                self.head.next = old_head

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """
        if node is self.tail:
            return None
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    def delete(self, node):
        """
        Deletes the input node from the List, preserving the
        order of the other elements of the List.
        """
        input_node = node
        prev_node = input_node.prev
        next_node = input_node.next

        if self.length == 0:
            return None
        elif not self.tail.prev and not self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            if self.head:
                self.remove_from_head()
            elif self.tail:
                self.remove_from_tail()
            else:
                # Reset prev_node's next
                prev_node.next = next_node

                # Reset next_node's previous
                next_node.prev = prev_node

                # Remove references
                input_node.next = None
                input_node.prev = None
                self.length -= 1

    def get_max(self):
        """
        Finds and returns the maximum value of all the nodes
        in the List.
        """
        current_node = self.head
        max_val = current_node.value
        while current_node is not None:

            if current_node.value > max_val:
                max_val = current_node.value

            current_node = current_node.next

        return max_val


if __name__ == "__main__":

    my_node = ListNode(1)
    my_list = DoublyLinkedList(my_node)
    # my_list.remove_from_head()

    my_list.add_to_tail(3)
    my_list.head.value  # > 1
    my_list.tail.value  # > 3

    my_list.move_to_front(my_list.tail)
    my_list.head.value  # > 3
    my_list.head.next.value
    # len(my_list)

    # at this stage, len == 2, head == 3, tail == 1
    # breakpoint()

    my_list.add_to_head(29)
    # my_list.head.value == 29
    # my_list.tail.value == 1
    # len == 3
    # my_list.head.next.value == 3
    my_list.move_to_front(my_list.head.next)
    my_list.head.value  # > 3
    breakpoint()
    my_list.head.next.value  # > 29
    len(my_list)  # > 3

    # breakpoint()
