#----------------Text Buffer------------------
#  1) Add characters from front and back
#  2) Remove characters from front and back
#  3) Render the contents of our buffer
#  4) Concatenate two buffers together (copying/pasting)

from doubly_linked_list.py import doubly_linked_list

class TextBuffer:
    def __init__(self, init=None):
        self.contents = DoublyLinkedList
        if init:
            for char in init:
                self.contents.add_to_tail(char)
    
    def __str__(self):
        pass
    
    def append(self, str_to_add):
        for char in str_to_add:
            self.contents.add_to_tail(char)
      
    def prepend(self, str_to_add):
        for char in str_to_add[::-1]:
            self.contents.add_to_head(char)
      
    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()
      
    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()

    def join(self, other_buffer):
        pass