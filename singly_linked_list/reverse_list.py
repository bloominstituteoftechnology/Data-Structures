def reverse_ll(ll):
    '''
    receive a LinkedList as input.
    returns reverse order linked list.
    '''

    if ll.head is None:
        return ll

    if ll.head is ll.tail:
        return ll

    current = ll.head
    while current is not None:
        