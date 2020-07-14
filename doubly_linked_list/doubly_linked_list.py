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
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):

        new_node: ListNode = ListNode(value)
        new_node.next: ListNode = self.head
        new_node.prev: ListNode = None

        self.length += 1
        if self.head is not None:
            self.head.prev = new_node

            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_from_head(self):

        target_to_delete = self.head

        if self.length == 0:

            return None

        elif self.length == 1:

            self.length -= 1
            self.head = None
            self.tail = None

            return target_to_delete.value

        else:
            self.head = target_to_delete.next
            self.length -= 1


            return target_to_delete.value









    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_node.prev: ListNode = self.tail
        new_node.next: ListNode = None

        self.length += 1
        if self.head is not None:
            self.head.next = new_node
        self.tail = new_node


    def remove_from_tail(self):
        pass


    def move_to_front(self, node):
        pass


    def move_to_end(self, node):
        pass


    def delete(self, node):
        pass


    def get_max(self):
        pass


dd = DoublyLinkedList()
dd.add_to_head(2)
print(dd.head.value)
print(dd.tail.value)



