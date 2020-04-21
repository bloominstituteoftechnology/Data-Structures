class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(node):
    head = node
    new_head = node.next
    node.next = None
    while new_head:
        future_head = new_head.next
        new_head.next = head
        head = new_head
        new_head = future_head
    return head

a = Node(1)
b = Node(2)
a.next = b
c = Node(3)
b.next = c
d = Node(4)
c.next = d
e = Node(5)
d.next = e

forward = a
print("Forward")
while forward is not None:
    print(forward.value)
    forward = forward.next

print("Reversed")
reversed = reverse(a)
while reversed is not None:
    print(reversed.value)
    reversed = reversed.next