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
        # self.value = None


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
        arrow = ' <-> '
        output += f'({curr_node.value}){arrow}'
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'({curr_node.value}){arrow}'
        return output[:-len(arrow)]

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
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
        deleted_value = self.head.value
        next_node = self.head.next
        self.head.delete()
        self.head = next_node
        self.length -= 1
        return deleted_value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
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
        deleted_value = self.tail.value
        prev_node = self.tail.prev
        self.tail.delete()
        self.tail = prev_node
        self.length -= 1
        return deleted_value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.add_to_head(node.value)
        if self.tail.value == node.value:
            self.tail = self.tail.prev
        node.delete()

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        if self.head.value == node.value:
            self.head = self.head.next
        node.delete()

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        curr_node = self.head
        if curr_node is None:
            return
        max_val = 0
        while curr_node is not None:
            if curr_node.value > max_val:
                max_val = curr_node.value
            curr_node = curr_node.next
        return max_val


node = ListNode(1)
dll = DoublyLinkedList(node)
dll.add_to_head(5)
dll.add_to_head(10)
print(dll)

print("TEST add_to_head")
dll.add_to_head(6)
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')

print("TEST remove_from_head")
deleted = dll.remove_from_head()
print(f'removed: {deleted}')
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')


print("TEST add_to_tail")
dll.add_to_tail(23)
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')


print("TEST remove_from_tail")
removed = dll.remove_from_tail()
print(f'removed: {removed}')
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')

print("TEST move_to_front")
print(f'node: {node.value}')
dll.move_to_front(node)
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')

print("TEST move_to_end")
print(f'node: {node.value}')
dll.move_to_end(node)
print(dll)
print(f'head: {dll.head.value}')
print(f'tail: {dll.tail.value}')
