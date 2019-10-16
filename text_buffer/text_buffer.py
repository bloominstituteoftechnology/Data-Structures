import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self, init=None):
        self storage = DoublyLinkedList()

        if init:
            for char in init:
                self.storage.add_to_tail(char)
    def __str__(self):
        s = ""
        current = self.storage.head

        while current:
            s += current.value
            current = current.next
        return s
    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)
    def prepend(self, string_to_add):
        for char in string_to_add[::-1]:
            self.storage.add_to_head(char)
    def delete_front(self, chars_to_remove):
        pass
    def delete_back(self, chars_to_remove):
        pass
    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        other_buffer.storage.head = self.contents.head
        self.storage.tail = other_buffer.storage.tail
        
    def split(self, split_location):
        pass
    def join_string(self, string_to_join):
        pass
