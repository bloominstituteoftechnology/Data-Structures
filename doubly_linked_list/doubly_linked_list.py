class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        ln = ListNode(value)
        if self.next is None:
            ln.prev = self
            self.next = ln
        else:
            self.next.prev = ln
            ln.next = self.next
            self.next = ln
        return self

    def insert_before(self, value):
        ln = ListNode(value)
        if self.prev is None:
            ln.next = self
            self.prev = ln
        else:
            self.prev.next = ln
            ln.prev = self.prev
            self.prev = ln
        return self

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self = None


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
        elif self.head.next is not None:
            self.head = self.head.insert_before(value)
        else:
            temp = self.head
            self.head = ListNode(value)
            self.head.next = temp
            temp.prev = self.head

    def remove_from_head(self):
        if self.head is not None:
            if self.head.next is not None:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                return temp.value
        else: return None

    def add_to_tail(self, value):
        ln = ListNode(value)
        if self.tail is None:
            self.tail = ln
        else:
            self.tail.next = ln
            ln.prev = self.tail
            self.tail = ln

    def remove_from_tail(self):
        if self.tail is not None:
            if self.tail.prev is not None:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                return temp.value
        else: return None

    def move_to_front(self, node):
        search = self.head
        found = False
        while found is False:
            if search.value == node.value:
                found = True
            else:
                search = search.next
        if found is True:
            temp = search
            if search.prev is not None:
                search.prev.next = search.next
            if search.next is not None:
                search.next.prev = search.prev
            self.add_to_head(search.value)
            search = None
        else: return None

    def move_to_end(self, node):
        search = self.head
        found = False
        while found is False:
            if search.value == node.value:
                found = True
            else:
                search = search.next
        if found is True:
            temp = search
            if search.prev is not None:
                search.prev.next = search.next
            if search.next is not None:
                search.next.prev = search.prev
            self.add_to_tail(search.value)
            search = None
        else: return None

    def delete(self, node):
        search = self.head
        found = False
        while found is False:
            if search.value == node.value:
                found = True
            else:
                search = search.next
        if found is True:
            search.delete()
        else: return None
        
