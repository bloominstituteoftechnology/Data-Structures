class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def return_middle(head):
    new_head = head
    current = head
    length = 0
    should_decapatate = False

    while current.next is not None:
        if length <= 2:
            new_head = head
        else:
            if should_decapatate:
                new_head = head.next
        length += 1
        current = current.next
        should_decapatate = not should_decapatate

    return new_head.value

a = Node(1)
b = Node(2)
a.next = b
c = Node(3)
b.next = c
d = Node(4)
c.next = d
e = Node(5)
d.next = e

print(return_middle(a))

class Node(object):
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next_node = next_node
   def __str__(self):
       return f"{self.data} : {self.next_node}"

    def reverse_list(list_head):
	length_index = 0
current_node = list_head
while current_node.next_node != None:
   		length_index += 1
   		current_node = current_node.next_node
while length_index > 0:
   		current_node = list_head
   		index = 0
  		while index != length_index:
       		current_node.data, current_node.next_node.data =\
         			current_node.next_node.data, current_node.data
       		current_node = current_node.next_node
       		index += 1
   		length_index -= 1