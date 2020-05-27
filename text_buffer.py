import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __str__(self):
        string_to_return = ""

        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next

        return string_to_return

    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storgae.head.prev = self.storage.tail

        self.storage.tail = other_buffer.tail

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_from_front(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head()

    def delete_from_back(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_tail()
