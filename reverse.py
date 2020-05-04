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








def recursive_reverse(node):
    if node.next is None:
        return node
    node.next = None
    new_head = node.next
    future_head = recursive_reverse(new_head)
    new_head.next = node
    return future_head

# 123
#     23
#         3
#     3


# 1 234
#     2 34
#         3 4
#             4-back
#         43
#     432
# 4321

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
reversed = recursive_reverse(a)
while reversed is not None:
    print(reversed.value)
    reversed = reversed.next

word = "five"
def rev(word):
    if len(word) == 1:
        return word
    word = rev(word[1:]) + (word[0])
    return word

print(rev(word))