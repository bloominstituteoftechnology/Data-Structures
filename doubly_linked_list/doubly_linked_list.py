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

    def report(self):
        values = []
        current_node = self.head
        while current_node.value:
            values.append(current_node.value)
            if current_node.next:
                current_node = current_node.next
            else:
                break
        print(str(values))
        print("My DLL's head: " + str(self.head.value))
        if self.head.next:
            print("My DLL's head.next: " + str(self.head.next.value))
        else:
            print("No head.next")
        print("My DLL's tail: " + str(self.tail.value))
        print("My DLL's length: " + str(self.length) + "\n")

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            # In this case, the len(self.list) == 0, so it didn't have a head or tail
            self.tail = new_node
        self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        self.length -= 1
        if self.head.next:
            removed_node = self.head
            next_to_transfer = self.head.next.next
            self.head = self.head.next
            self.head.prev = None
            self.head.next = next_to_transfer
            return removed_node.value
        elif self.head:
            # In this case, len(self.list) == 1
            return_value = self.head.value
            self.head = None
            self.tail = None
            return return_value
        else:
            # In this case, len(self.list) == 0
            self.head = None
            self.tail = None
            return None

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            # In this case, the DLL was empty, so it didn't have a head.
            self.head = new_node
        self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        remove_node = self.tail
        if self.tail.prev:
            # In this case, the len(self.list) is > 1
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # In this case, len(self.list) == 1, so taking away the tail empties the DLL.
            self.tail = None
            self.head = None
        self.length -= 1
        return remove_node.value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # Delete the node from the list
        node.delete()
        self.length -= 1
        # Add it as the new head
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # Delete the node from the list
        if node == self.tail:
            # In this case, no need to continue
            return False
        new_head = None
        if self.length == 2:
            # In this case, the tail will become the head
            new_head = self.tail
        node.delete()
        self.length -= 1
        # Add node as the new tail
        self.add_to_tail(node.value)
        if new_head:
            self.head = new_head

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        winner = self.head.value
        current_node = self.head
        while current_node.value:
            if current_node.value > winner:
                winner = current_node.value
            if current_node.next:
                current_node = current_node.next
            else:
                break
        print("Max value: " + str(winner))
        return winner


'''
my_first_node = ListNode(1)
print("Add 1 as the head.")
my_dll = DoublyLinkedList(my_first_node)
my_dll.report()

print("Add 2 as the new head.")
my_dll.add_to_head(2)
my_dll.report()

print("Add 3 as the new head.")
my_dll.add_to_head(3)
my_dll.report()

print("Remove the head (3).")
my_dll.remove_from_head()
my_dll.report()

print("Add 3 as the new head.")
my_dll.add_to_head(3)
my_dll.report()

print("Add 10 as the new tail.")
my_dll.add_to_tail(10)
my_dll.report()

print("Add 20 as the new tail.")
my_dll.add_to_tail(20)
my_dll.report()

print("Remove from tail (20).")
my_dll.remove_from_tail()
my_dll.report()

print("Move the tail (10) as the new head")
new_head = my_dll.tail
my_dll.remove_from_tail()
my_dll.move_to_front(new_head)
my_dll.report()

print("Remove the head (10) and put it back as the new tail.")
new_tail = my_dll.head
my_dll.remove_from_head()
my_dll.move_to_end(new_tail)
my_dll.report()

print("Remove 10")
my_dll.delete(my_dll.tail)
my_dll.report()

print("Remove 2")
my_dll.delete(my_dll.tail.prev)
my_dll.report()

print("Get max value")
my_dll.get_max()
'''
