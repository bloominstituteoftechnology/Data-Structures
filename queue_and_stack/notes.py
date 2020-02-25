# how do you find and return the middle node of a singly linked list in one pass?

# you do not have access to the length of the list, if the list is even, return first of two middle nodes
# you may not store in another data structure, including another linked list
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode



class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    l = [9,2,5,3,7,4,6,8,1]
    llist = ListNode(l[0])
    for i in l:
        llist.insert_after(i)
    print(llist.value)


#runtime to remove from head or tail O(1)