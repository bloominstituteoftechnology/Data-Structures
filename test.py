#middle node: How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
        
print(mult(3,1))