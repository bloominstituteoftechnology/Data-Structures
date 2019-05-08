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
        return self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

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
        if self.head is None and self.tail is None:
            return 0
        else:
            current = self.head.next
            count = 1
            while current is not None:
                count += 1
                current = current.next
            self.length = count
        return self.length

    def add_to_head(self, value):
        new_node_head = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node_head
            self.tail = new_node_head
        else:
            x = self.head.insert_before(value)
            self.head = x

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            old_head_value = self.head.value
            self.head = None
            self.tail = None
            return old_head_value
        else:
            old_head_value = self.head.value
            self.head.delete()
            return old_head_value

    def add_to_tail(self, value):
        new_node_tail = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node_tail
            self.tail = new_node_tail
        else:
            x = self.tail.insert_after(value)
            self.tail = x

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            old_tail_value = self.tail.value
            self.head = None
            self.tail = None
            return old_tail_value
        else:
            old_tail_value = self.tail.value
            self.tail.delete()
            return old_tail_value

    def move_to_front(self, node):
        if node.prev == None:
            return
        else:
            if node == self.tail:
                self.tail = node.prev
            node_0 = node.next
            node_1 = node
            node_2 = node.prev
            node_3 = node.prev.prev

            node_1.prev = node_2.prev
            node_2.next = node_1.next
            node_2.prev = node_1
            node_1.next = node_2
            
            if node_0 is not None:
                node_0.prev = node_2
            if node_3 is not None:
                node_3.next = node_1
            self.head = node

            self.move_to_front(node)

    def move_to_end(self, node):
        if node.next == None:
            return
        else:
            if node == self.head:
                self.head = node.next
            node_0 = node.prev
            node_1 = node
            node_2 = node.next
            node_3 = node.next.next

            node_1.next = node_2.next
            node_2.next = node_1
            node_2.prev = node_1.prev
            node_1.prev = node_2
            
            if node_0 is not None:
                node_0.next = node_2
            if node_3 is not None:
                node_3.prev = node_1
            self.tail = node

            self.move_to_end(node)

    def delete(self, node):
        node.delete()
        if self.tail == node and self.head == node:
            self.tail = None
            self.head = None
        elif self.tail == node:
            self.tail = node.prev
        elif self.head == node:
            self.head = node.next

    def get_max(self):
        current = self.head
        max = 0
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max

# print('test10')
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# print(f"dll.get_max(): {dll.get_max()}")

# print('test10')
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# dll.delete(node)
# print(f"dll.tail: {dll.tail}")
# print(f"dll.head: {dll.head}")
# print(f"length: {len(dll)}")

# dll.add_to_tail(1)
# dll.add_to_head(9)
# dll.add_to_tail(6)

# dll.delete(dll.head)
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.head.value: {dll.head.value}")
# print(f"length: {len(dll)}")

# print('test9')
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# dll.add_to_tail(3)
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.head.value: {dll.head.value}")

# print(dll.move_to_front(dll.tail))
# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.next.value: {dll.head.next.value}")
# print(f"length: {len(dll)}")

# print('test8')
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# dll.add_to_head(40)
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.head.value: {dll.head.value}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(dll.move_to_end(dll.head))
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev.value: {dll.tail.prev.value}")
# print(f"length: {len(dll)}")

# dll.add_to_tail(4)
# print(dll.move_to_end(dll.head.next))
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev.value: {dll.tail.prev.value}")
# print(f"length: {len(dll)}")

# test1
# node = ListNode(1)
# dll = DoublyLinkedList(node)
# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(f"dll.remove_from_tail(): {dll.remove_from_tail()}")

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"length: {len(dll)}") # not sure

# dll.add_to_tail(33)
# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(f"length: {len(dll)}") # not sure

# print(f"dll.remove_from_tail(): {dll.remove_from_tail()}")

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"length: {len(dll)}") # not sure

# dll.add_to_tail(68)

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(f"dll.remove_from_tail(): {dll.remove_from_tail()}")

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"length: {len(dll)}") # not sure

# #### test2
# dll = DoublyLinkedList(node)

# print(f"dll.remove_from_head(): {dll.remove_from_head()}")

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"length: {len(dll)}") # not sure

# dll.add_to_head(2)
# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(f"length: {len(dll)}") # not sure
# print(f"dll.remove_from_head(): {dll.remove_from_head()}")
# print(f"length: {len(dll)}") # not sure

# dll.add_to_head(55)
# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.prev: {dll.head.prev}")
# print(f"dll.head.next: {dll.head.next}")

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"dll.tail.prev: {dll.tail.prev}")
# print(f"dll.tail.next: {dll.tail.next}")

# print(f"length: {len(dll)}") # not sure
# print(f"dll.remove_from_head(): {dll.remove_from_head()}")
# print(f"length: {len(dll)}") # not sure

# #### test3
# dll = DoublyLinkedList(node)

# print(f"dll.tail.value: {dll.tail.value}")
# print(f"length: {len(dll)}") # not sure

# dll.add_to_tail(30)

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.tail.prev.value: {dll.tail.prev.value}")
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"length: {len(dll)}") # not sure

# dll.add_to_tail(20)

# print(f"head: {dll.head}")
# print(f"tail: {dll.tail}")

# print(f"dll.tail.prev.value: {dll.tail.prev.value}")
# print(f"dll.tail.value: {dll.tail.value}")
# print(f"length: {len(dll)}") # not sure

# #### test4

# node_1 = ListNode(3)
# node_2 = ListNode(4)
# node_3 = ListNode(5)
# print(f"node_1: {node_1}")
# print(f"node_2: {node_2}")
# print(f"node_3: {node_3}")

# node_1.next = node_2
# node_2.next = node_3
# node_2.prev = node_1
# node_3.prev = node_2

# node_2.delete()

# print(f"node_1.next: {node_1.next}")
# print(f"node_3.prev: {node_3.prev}")

# #### test5
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# node.insert_before(0)
# print(f"node.prev.value: {node.prev.value}")

# #### test6
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# print(f"dll.head.value: {dll.head.value}")

# dll.add_to_head(10)
# print(f"dll.head.value: {dll.head.value}")
# print(f"dll.head.next: {dll.head.next.value}")
# print(f"length: {len(dll)}") # not sure

# #### test7
# node = ListNode(1)
# dll = DoublyLinkedList(node)

# node.insert_after(2)
# print(f"node.next.value: {node.next.value}")
