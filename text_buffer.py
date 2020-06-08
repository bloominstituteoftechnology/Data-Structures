# File I/O Future release

# add to back of text buffer
#add toy front of text buffer
# join 2 buffers 

#delete to back of buffer
# delete to front of buffer 
# add to middle

# Array vs DLL
# array : add to back : O(1)
#array : add to back : O(n)
# delete from back : O(1)
# delete from front : O(n)
# join text buffers : O(n) --> walk accross 2 arrays and put them to another array 
#

# DLL
# add to back : O(1)
#add to front : O(1)
# delete from front and back : O(1) 
# Join 2 DLLs : O(1)

#__str__ : to print out whats inside 
# Array : O(n)
# DLL: O(n) 

import sys 
sys.path.append("./doubly_linked_list")
from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def append(self,str_to_add):

        for char in str_to_add:
            self.storage.add_to_tail(char)

    def prepend(self,str_to_add):
        for char in str_to_add:
            self.storage.add_to_head(char)

    def join(self, other_buffer):
        #linktail of this buffer to head of other buffer
        self.storage.tail.next=other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        #point out tail to new tail 
        self.storage.tail=other_buffer.storage.tail
        

    def __str__(self):

        string_to_return=""
        node=self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next
        return string_to_return

    def delete_from_front(self,num_char_to_remove):
        for _ in range (num_char_to_remove):
            self.storage.remove_from_head()
    
    def delete_from_back(self,num_char_to_remove):
        for _ in range(num_char_to_remove):
            self.storage.remove_from_tail()

    def find_text(self,text_to_find):
        pass

    

