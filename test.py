#middle node: How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.
class daynames:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')
e5 = daynames('Fri')

e1.next_value = e3
e3.next_value = e2
e2.next_value = e4
e4.next_value = e5


# thisvalue = e1

while e1:
        print(e1.value)
        e1 = e1.next_value

class number:
    def __init__(self, value):
        self.value = value
        self.next_v = None

n1 = number('one')
n2 = number('Tow')
n3 = number('three')

n1.next_v = n2
n2.next_v = n3

while n1:
    print(n1.value)
    n1 = n1.next_v
    