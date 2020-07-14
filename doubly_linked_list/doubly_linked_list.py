
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

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node = self.head
            new_node = ListNode(value, next=current_node)
            current_node.prev = new_node
            self.head = new_node
            self.length += 1

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
        # inserts it as new head node of the List
        # self.head = node
        pass

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """
        pass

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
        pass

if __name__ == "__main__":
    
    my_node = ListNode(1)
    my_list = DoublyLinkedList(my_node)
    # my_list.remove_from_head()

    my_list.delete(my_list.head)
    my_list.add_to_tail(1)
    my_list.add_to_head(9)
    my_list.add_to_tail(6)
    my_list.delete(my_list.head)
    
    breakpoint()