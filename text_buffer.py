# file I/O - for another day

# add to the back of a text buffer
# add to the front of a text buffer
# delete from the back of a text buffer
# delete from the front of a text buffer

# join text buffers together

# add to middle

""" array vs DLL (doubly linked list)
array: add to back O(1) complexity
array: add to front O(n) complexity
array: delete from the back O(1) complexity
array: delete from the front O(n) complexity
array: join text buffers together: O(n) complexity
array: __str__, to print O(n) complexity


DLL: add to back O(1) complexity
DLL: add to front O(1) complexity
DLL: delete from back O(1) complexity
DLL: delete from front O(1) complexity
DLL: join text buffers together O(1) complexity
DLL: __str__, to print O(n) complexity
"""
import sys

sys.path.append('./doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()
        
    def __str__(self):
        str_to_return = ""
        node = self.storage.head
        
        while node is not None:
            str_to_return += node.value
            node = node.next
    
    def join(self, string_to_add):
        #link tail of first buffer to the head of the other buffer
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        self.storage.tail = other_buffer.storage.tail
        
    def append (self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)
    
    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)
    
    def delete_from_front(self, number_of_chars_to_remove):
        for x in range(number_of_chars_to_remove):
            self.storage.remove_from_head()
    
    def delete_from_back(self, number_of_chars_to_remove):
        for x in range(number_of_chars_to_remove):
            self.storage.remove_from_tail()
    
    def find_text(self, text_to_find):
        pass
    
text = TextBuffer()
text.append('Hello')
    
print(text)