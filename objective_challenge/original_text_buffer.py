from doubly_linked_list import DoublyLinkedList 

class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat 
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            self.contents.add_to_head(init)

    def __str__(self):
        # needs to return a string to print 
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        if string_to_add.isascii():
            self.contents.head.value += string_to_add

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct 
        # order when adding to the front of the text buffer 
        if string_to_add.isascii():
            self.contents.head.value = string_to_add + self.contents.head.value

    def delete_front(self, chars_to_remove):
        self.contents.head.value = self.contents.head.value[chars_to_remove:]

    def delete_back(self, chars_to_remove):
        self.contents.head.value = self.contents.head.value[:len(self.contents.head.value) - chars_to_remove]

    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer 
    The tail of the concatenated buffer will be the tail of the other buffer 
    The head of the concatenated buffer will be the head of this buffer 
    """
    def join(self, other_buffer):
        # we might want to check that other_buffer is indeed a text buffer 
        # set self list tail's next node to be the head of the other buffer
        # set other_buffer head's prev node to be the tail of this buffer
        if other_buffer.contents.head.value.isascii():
            self.contents.head.value += other_buffer.contents.head.value
        
    # if we get fed a string instead of a text buffer instance,
    # initialize a new text buffer with this string and then 
    # call the join method 
    def join_string(self, string_to_join):
        if string_to_join.isascii():
            self.contents.head.value += string_to_join

if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

    text.join_string("califragilisticexpealidocious")
    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)
