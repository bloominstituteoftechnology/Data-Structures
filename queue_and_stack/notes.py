# how do you find and return the middle node of a singly linked list in one pass?

# you do not have access to the length of the list, if the list is even, return first of two middle nodes
# you may not store in another data structure, including another linked list
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode

l = [9,2,5,3,7,4,6,8,1]

linkedlist = ListNode(l[0])
for i in range(1, len(l)):
    linkedlist.insert_after(l[i])
print(linkedlist.next.value)

