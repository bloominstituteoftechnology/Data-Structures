from doubly_linked_list import DoublyLinkedList


# return middle node of the DLL, if there are two, return the left
# no empty list, length >= 1
# we do not know the length
# 1-2-3 : 2
# 1-2-3-4 : 2
def find_middle(dll):
    head = dll.head
    tail = dll.tail

    while head != tail and head.next != tail:
        head = head.next
        tail = tail.prev

    return head.value


odd_nums = DoublyLinkedList()
[odd_nums.add_to_tail(i) for i in [5, 6, 3, 4, 10, 6, 7]]
print(find_middle(odd_nums))
even_nums = DoublyLinkedList()
[even_nums.add_to_tail(i) for i in [5, 3, 4, 10, 7]]
print(find_middle(even_nums))

stupid_num = DoublyLinkedList()
[stupid_num.add_to_tail(i) for i in range(1, 100000)]
print(find_middle(stupid_num))
