class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = ListNode(value) if value else None
        self.tail = None
        self.length = 1 if value else 0
    def __len__(self):
        return self.length
    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
    def contains(self, value):
        node = self.head
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False
    def remove_head(self):
        if self.head == None:
            return None
        prev_head = self.head
        self.head = prev_head.next
        if self.head == None:
            self.tail = None 
        self.length -= 1
        return prev_head.value
    def get_max(self):
        max_val = float("-inf")
        node = self.head
        while node != None:
            if node.value > max_val:
                max_val = node.value
            node = node.next
        return max_val if self.head else None