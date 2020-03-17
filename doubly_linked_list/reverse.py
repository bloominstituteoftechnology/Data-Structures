from doubly_linked_list import DoublyLinkedList


# no recursion
# cannot store dll and data in other structures

def reverse(dll):
    current = dll.head
    # this will be our new tail
    current.next = None
    while current.next is not None:
        curr_next = current.next

        curr_next.next = current
        current.next = curr_next.next


dumb = DoublyLinkedList()
[dumb.add_to_tail(i) for i in range(1, 10)]
print(reverse(dumb))
