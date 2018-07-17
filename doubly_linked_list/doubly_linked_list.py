class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        new_node = ListNode(value, self, self.next)
        self.next = new_node

    def insert_before(self, value):
        new_node = ListNode(value, self.prev, self)
        self.prev = new_node

    def delete(self):
        if not self.next:
            self.prev.next = None
        elif not self.prev:
            self.next.prev = None
        else:
            next_node = self.next
            prev_node = self.prev

            next_node.prev = prev_node
            prev_node.next = next_node


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if not self.head:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        value = self.head.value
        self.head = self.head.next
        # self.head.prev = None
        self.head.insert_before(None)
        return value

    def add_to_tail(self, value):
        if not self.tail:
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        value = self.tail.value
        self.tail = self.tail.prev
        # self.tail.next = None
        self.tail.insert_after(None)
        return value

    # def move_to_front(self, node):
    #     current = self.head
    #     while current:
    #         if current.value == node.value:
    #             self.head.insert_before(node.value)
    #             current.delete()
    #             self.head = self.head.prev
    #             return self.head.value
    #         else:
    #             current = current.next
    #     return False

    def move_to_front(self, node):
        head = self.head
        headValue = head.value
        tail = self.tail
        tailValue = tail.value
        while head.value != tailValue and tail.value != headValue:
            if headValue == node.value:
                self.head.insert_before(node.value)
                head.delete()
                self.head = self.head.prev
                return self.head.value
            if tailValue == node.value:
                self.head.insert_before(node.value)
                tail.delete()
                self.head = self.head.prev
                return self.head.value
            else:
                head = head.next
                tail = tail.prev
        return False

    # def move_to_end(self, node):
    #     current = self.tail
    #     while current:
    #         if current.value == node.value:
    #             self.tail.insert_after(node.value)
    #             current.delete()
    #             self.tail = self.tail.next
    #             return self.tail.value
    #         else:
    #             current = current.prev
    #     return False

    def move_to_end(self, node):
        pointer_end = self.tail
        pointer_front = self.head

        while pointer_end and pointer_front:
            if pointer_end == pointer_front:
                print('fire')
                break
            if pointer_end.value == node.value:
                self.tail.insert_after(node.value)
                pointer_end.delete()
                self.tail = self.tail.next
                return self.tail.value
            elif pointer_front.value == node.value:
                self.tail.insert_after(node.value)
                pointer_front.delete()
                self.tail = self.tail.next
                return self.tail.value
            else:
                pointer_end = pointer_end.prev
                pointer_front = pointer_front.next

        return False

    def delete(self, node):
        node.delete()
        return node
