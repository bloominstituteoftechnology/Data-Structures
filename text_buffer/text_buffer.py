from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            self.append(init)

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        for c in string_to_add:
            self.contents.add_to_tail(c)

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct
        # order when adding to the front of the text buffer
        for c in string_to_add[::-1]:
            self.contents.add_to_head(c)

    def delete_front(self, chars_to_remove):
        while chars_to_remove:
            self.contents.remove_from_head()
            chars_to_remove -= 1

    def delete_back(self, chars_to_remove):
        while chars_to_remove:
            self.contents.remove_from_tail()
            chars_to_remove -= 1

    # for i in range(chars_to_remove):
    #     self.contents.remove_from_tail()
    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer 
    The tail of the concatenated buffer will be the tail of the other buffer 
    The head of the concatenated buffer will be the head of this buffer 
    """

    def join(self, other_buffer):
        # we might want to check that other_buffer is indeed a text buffer
        # set self list tail's next node to be the head of the other buffer

        if isinstance(other_buffer, TextBuffer):
            self.contents.tail.next = other_buffer.contents.head
            other_buffer.contents.head.prev = self.contents.tail
            self.contents.tail = other_buffer.contents.tail
            self.contents.length += other_buffer.contents.length
        else:
            print("ERROR: arg is not a text buffer")
            return
            # set other_buffer head's prev node to be the tail of this buffer

            # if we get fed a string instead of a text buffer instance,
            # initialize a new text buffer with this string and then
            # call the join method

    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)


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
