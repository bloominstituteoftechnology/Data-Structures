# a single node of singly linked list
class ListNode:
    # constructor
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# single node
my_list = ListNode(3)
print(my_list.val)


# Linked List class with a single head node
class SingleLink:
    def __init__(self):
        self.head = None

    # insertion method
    def insert(self, val):
        new_node = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # code a print method
    def print_link_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next


# Linked List with a single node
LinkList = SingleLink()
# LinkList.head = ListNode(3)
# print(LinkList.head.val)
LinkList.insert(5)
LinkList.insert(10)
LinkList.insert(15)
LinkList.print_link_list()
