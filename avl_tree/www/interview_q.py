# How do you find and return the middle node of a singly linked list in one pass? 
# You do not have access to the length of the list. 
# If the list is even, you should return the first of the two "middle" nodes. 
# You may not store the nodes in another data structure.

# P
# 

class Node:
    def __init__(self, node):
        self.node = node
        self.next = None


    # of the two "middle" nodes.
    
    # increment when its the odd  
    # we inc var if its odd or even
    # if its even its stays the same 
    # if its odd increment 
    
def find_middle(node):
    current = node

    second_pointer = node.next
        
   
    
    while node:
        if second_pointer.next is None:
            return "Middle node is %s" % str(current.node)
        if second_pointer.next.next is None:
            return "Middle node is %s" % str(current.node)
        else:
            current = current.next
            second_pointer = second_pointer.next.next
            


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
# node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6

print(find_middle (node1))
print(find_middle (node1))

