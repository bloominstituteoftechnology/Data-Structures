class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def contains(self, value):
        res = False
        curr_node = self.head

        while curr_node != None:
            if curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next

        return res

    def remove_head(self):
        if self.head:
            value = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return value

    def get_max(self):
        if not self.head:
            return
        if self.head == self.tail:
            return self.head.value

        max = 0
        curr_node = self.head

        while True:
            if curr_node.value > max:
                max = curr_node.value
            if curr_node.next == None:
                break
            else:
                curr_node = curr_node.next

        return max
