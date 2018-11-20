class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        temp = self.next
        new_node = ListNode(value)
        new_node.prev = self
        self.next = new_node
        if temp is not None:
            temp.prev = new_node

    def insert_before(self, value):
        temp = self.prev
        new_node = ListNode(value)
        new_node.next = self
        self.prev = new_node
        if temp is not None:
            temp.next = new_node

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        if self.head is not None:
            temp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            return temp.value

    def add_to_tail(self, value):
        if self.head is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        if self.tail is not None:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp.value

    def move_to_front(self, node):
        temp = self.head
        while temp:
            if node.value == temp.value:
                break
            temp = temp.next
        temp.delete()
        self.add_to_head(temp.value)

    def move_to_end(self, node):
        temp = self.head
        while temp:
            if node.value == temp.value:
                break
            temp = temp.next
        temp.delete()
        self.add_to_tail(temp.value)

    def delete(self, node):
        temp = self.head
        while temp:
            if node.value == temp.value:
                break
            temp = temp.next
        temp.delete()
