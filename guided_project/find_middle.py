
from '../doubly_linked_list/doubly_linked_list.py' import DoublyLinkedList

def find_middle(dll):
	# return the middle node of the DLL, if there are two nodes, return the left None
	# 1-2-3: 2
	# 5-3-4-10-7: 4
	# no empty list,
	# length >= 1
	# not sorted,
	# single pass solution,
	# dont know the length
	# which direction


	#5/2 = 2.5
	#4/2 = 2
	head = dll.head
	tail = dll.tail

	while head != tail and head.next != tail:
		head = head.next
		tail = tail.prev


odd_nums = DoublyLinkedList()
[odd_nums.add_to_head(i) for i in [7,10,4,3,5]]
print(find_middle(odd_nums))


even_nums = DoublyLinkedList()
[odd_nums.add_to_head(i) for i in [5,3,4,'10',3,5]]
odd_nums.add_to_head(7,10,4,3)
	# traverse the dll using while
	#if  dll length is even, get
 	#if  dll length is odd, get the floor of the dll/2




