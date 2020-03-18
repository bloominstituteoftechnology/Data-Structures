import sys
from doubly_linked_list import DoublyLinkedList

# no recursion
# we cannot store the DLL and its data in other data structure
def reverse(dll):
	current = dll.head

	while current.next is not None:
		current.next.prev = current
		current.prev.next =
		'''curr_next = current.next
		curr_prev = current.prev
		current.next = curr_prev
		current.prev = curr_next'''



even_nums = DoublyLinkedList()
even_nums.add_to_head(1)
even_nums.add_to_head(2)
even_nums.add_to_head(3)
even_nums.add_to_head(4)
even_nums.add_to_head(5)
even_nums.add_to_head(6)
even_nums.add_to_head(7)
even_nums.add_to_head(8)
even_nums.add_to_head(9)
even_nums.add_to_head(10)
print(reverse(even_nums))