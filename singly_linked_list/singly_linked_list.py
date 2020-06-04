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

    def prepend(self, value):
        old_head = self.head
        self.head = ListNode(value, old_head)

    def append(self, value):
        self.tail.next_node = value

    def remove_from_head(self) -> ListNode:
        if self.head is None:
            return None
        old_head = self.head
        self.head = old_head.next_node
        return old_head
