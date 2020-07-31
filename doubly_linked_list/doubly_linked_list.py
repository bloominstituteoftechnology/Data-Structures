"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        else:
            return
        if self.next:
            self.next.prev = self.prev
        else:
            return
            # 1 <-> 2 <-> 3


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
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if node is already at the front
        if node is self.head:
            return
        value = node.value
        # if node is at tail
        if node is self.tail:
            self.remove_from_tail()
        # if node is somewhere else
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if node is already at the end
        if node is self.tail:
            return
        value = node.value
        # if node is at the head
        if node is self.head:
            self.remove_from_head()
        # if anywhere else
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)
        # had self.add_to_tail(value) so silly mistake like that

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if there's nothing in list
        if not self.head:
            return
        # if there's one item in the list
        elif (self.head is node) & (self.tail is node):
            self.head = None
            self.tail = None
            self.length -= 1
        # value is in head
        elif self.head is node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        # if value is in tail
        elif self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        # if in middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        # Multiple if's means your code would go and check all the if conditions, where as in case of elif,
        # if one if condition satisfies it would not check other conditions..
        # SO BASICALLY: the elif makes the if statement STICK TOGETHER
        # SO BASICALLY: the elif makes the if statement STICK TOGETHER

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        # if lists is empty
        if not current:
            return
        # if there's only one thing in the list
        if current.next is None:
            return current.value
        max = current.value
        while current is not None:
            if max < current.value:
                max = current.value
            current = current.next
        return max


if __name__ == '__main__':
    node = ListNode(1)
    dll = DoublyLinkedList(node)
    dll.add_to_tail(6)
    dll.move_to_end(dll.head)
    print(dll.head.value)
    print(dll.tail.value)