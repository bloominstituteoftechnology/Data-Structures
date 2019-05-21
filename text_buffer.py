from collections import deque

""" 
alt shift a == comment block 
dir(name of data type)
help(dict)
What sort of operations do we need to be able to perform with a text editor?
- Insertion 
    - prepend - add to the front
    - append  - add to the back
- Deletion - from the front and the back
- Copy/Pasting

Ideally we want O(1) time complexity for every operation.
- An array wouldn't work. O(n) for prepending and deleting from the front.
- Linked List sounds good
    - Probably a doubly linked list.

"""

class TextBuffer:
    def __init__(self, initial_text=None):
        self.contents = DoublyLinkedList()
        if initial_text:
            for char in inital_text:
                self.contents.add_to_tail(char)
        
        #print the conatent of our text buffer?
        def __repr__