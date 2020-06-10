class ListNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node: ListNode = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.length = 0 if head is None else 1

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        old_head = self.head
        self.head = ListNode(value, old_head)
        self.length += 1

    def add_to_tail(self, value):
        # print(f"LL: adding value {value} to tail")
        new_node = ListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    # O(1)
    def remove_head(self):
        if self.head is None:
            # print("LL: returning None from head")
            return None
        old_head = self.head
        self.head = old_head.next_node
        self.length -= 1
        # print(f"LL: returning old head value: '{old_head.value}'")
        if self.head is None:
            self.tail = None
        return old_head.value

    # O(n)
    def remove_tail(self):
        if self.tail is None:
            return None
        n = self.head
        while n.next_node is not None \
                and n.next_node.next_node is not None:
            n = n.next_node
        output = n.next_node.value
        self.tail = n
        self.tail.next_node = None
        self.length -= 1
        return output

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
