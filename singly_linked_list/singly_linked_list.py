class ListNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node: ListNode = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        return self.length

    @property
    def tail(self) -> ListNode:
        if self.head is None:
            return None
        node = self.head
        while node.next_node is not None:
            node = node.next_node
        return node

    @property
    def length(self) -> int:
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next_node
        return count

    def add_to_head(self, value):
        old_head = self.head
        self.head = ListNode(value, old_head)

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node

    def remove_head(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = old_head.next_node
        return old_head.value

    def get_max(self):
        current = self.head
        if current is None:
            return None
        current_max = current.value
        while current is not None:
            current_max = max(current_max, current.value)
            current = current.next_node
        return current_max

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        return False
