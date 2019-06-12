from linked_list import LinkedList

def check_for_cycle(ll):
    pass


# Tests
ll = LinkedList()

print(check_for_cycle(ll))
# should print False

ll.add_to_tail(1)

print(check_for_cycle(ll))
# should print False

ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)

print(check_for_cycle(ll))
# should print False

ll.tail.next = ll.head.next.next

print(check_for_cycle(ll))
# should print True
