from doubly_linked_list import DoublyLinkedList


def reverse_link_list(head):
    prevNode = None

    while head != None:
        tempNextNode = head.next
        head.next = prevNode
        prevNode = head
        head = tempNextNode
    return prevNode
