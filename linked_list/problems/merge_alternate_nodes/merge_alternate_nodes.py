from linked_list import LinkedList

def merge_alternate_nodes(alist, blist):
    pass 


# Tests
alist = LinkedList()
blist = LinkedList()

alist.add_to_tail('a')
alist.add_to_tail('b')
alist.add_to_tail('c')

blist.add_to_tail(1)
blist.add_to_tail(2)
blist.add_to_tail(3)

print(merge_alternate_nodes(alist, blist))
# should print 

alist = LinkedList()
blist = LinkedList()

alist.add_to_tail('x')

blist.add_to_tail(10)
blist.add_to_tail(20)
blist.add_to_tail(30)

print(merge_alternate_nodes(alist, blist))
# should print 

alist = LinkedList()
blist = LinkedList()

alist.add_to_tail('i')
alist.add_to_tail('j')
alist.add_to_tail('k')

print(merge_alternate_nodes(alist, blist))
# should print 
