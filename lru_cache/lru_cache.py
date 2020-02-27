

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

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

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
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, next=self.head)
        if not self.head:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        value = self.head.value
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if not self.head:
            self.head = self.tail = ListNode(value)
        else:
            self.tail = ListNode(value, prev=self.tail)
            self.tail.prev.next = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        if self.head == self.tail:
            self.tail.delete()
            self.head = None
            self.tail = None
        self.length -= 1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.add_to_head(node.value)
        node.delete()
        self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        current_node = self.head.next
        max_node = self.head.value
        while current_node:
            if current_node.value > max_node:
                max_node = current_node.value
            current_node = current_node.next
        return max_node


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    def __str__(self):
        return f'I am storage: {self.storage}'

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        value = None
        if key in self.storage:
            node = self.storage[key]
            value = node.value[1]
            self.cache.move_to_front(node)
            # return node.value[1]
        else:
            return value

        # if key in self.storage:
        #     storage_node = self.storage[key]
        #     self.cache.move_to_front(storage_node)
        #     return self.storage[key].value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # node = [key, value]
        if key in self.storage is not None:
            node = self.storage[key]
            node.value = [key, value]
            self.cache.move_to_front(node)

            return
        if self.size == self.limit:
            del self.storage[self.cache.tail.value[0]]
            self.cache.remove_from_tail()
            self.size -= 1

        self.cache.add_to_head([key, value])
        self.storage[key] = self.cache.head
        self.size += 1

        # if key in self.storage:
        #     # retrieve key value node
        #     storage_node = self.storage[key]
        #     # update key value
        #     storage_node.value[1] = value
        #     # move node to top of stack
        #     self.cache.move_to_front(storage_node)
        # else:
        #     self.cache.add_to_head([key, value])
        #     self.storage[key] = self.cache.head
        #     if self.size >= self.limit:
        #         # remove the last value
        #         del self.storage[self.cache.tail.value[0]]
        #         self.cache.remove_from_tail()
        #     else:
        #         # cache wasn't full; increase size
        #         self.size += 1


test = LRUCache(3)
test.set('item1', 'a')
test.set('item2', 'b')
test.set('item3', 'c')


print('I am storage: ', test.storage)


# print('\n')
# print(test.get('item1'))
# print('\n')
# print('I am storage: ', test.storage)
