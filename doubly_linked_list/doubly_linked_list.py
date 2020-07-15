# doubly_linked_list/doubly_linked_list.py

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next_ = next_

    def delete(self):
        if self.prev:
            self.prev.next_ = self.next_
        elif self.next_:
            self.next_.prev = self.prev
        
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
        self.length += 1

        # Adding node to an empty list:
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Adding node to a non-empty list:
        else:
            new_node.next_ = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head_value = self.head.value
        self.delete(self.head)
        return head_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # Adding node to an empty list:
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Adding node to a non-empty list:
        else:
            new_node.prev = self.tail
            self.tail.next_ = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # moving the head --> do nothing
        if node == self.head:
            return
        # moving the tail
        # general case
        else:
            old_value = node.value
            self.delete(node)
            self.add_to_head(old_value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # moving the tail --> do nothing
        if node == self.tail:
            return
        # moving the head
        # general case
        else:
            old_value = node.value
            self.delete(node)
            self.add_to_tail(old_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        # deleting from empty list --> do nothing:
        if self.head is None and self.tail is None:
            return
        # deleting from a single-node list:
        elif self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # deleting the head node, self.list >= 2
        elif node == self.head:
            self.head = node.next_
            node.delete()
        # deleting the tail node, self.list >= 2
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        # general case node --> delete
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head or not self.tail:
            return None

        max_value = self.head.value

        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next_
        return max_value

    """
    Finds and returns the minimum value of all the nodes 
    in the List.
    """
    def get_min(self):
        if not self.head or not self.tail:
            return

        min_value = self.head

        current = self.head.next_
        while current:
            if current.value < min_value:
                min_value = current.value
            current = current.next_
        return min_value


if __name__ == "__main__":
    node = ListNode(1)
    dll = DoublyLinkedList(node)
    print(dll.get_max()) # --> 1, PASS

    dll.add_to_tail(100)

    # This line breaks things...
    print(dll.get_max())

