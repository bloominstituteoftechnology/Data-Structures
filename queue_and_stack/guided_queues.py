# First Class Guided Problem Specification:
# How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two “middle” nodes. You may not store the nodes in another data structure.


# PLAN
# Iterate through the LIST, with two (2) variable markers for the current last and current middle node. Update the middle node every other new tail node.

# when the last variable reaches the actual tail, figure out if odd or even

# if odd, return the single middle marker variable
# if even, return the first of two middle marker variables

def findMiddle(singly_linked_list):

    # edge case: List was empty all along
    # Return None since there are no nodes
    if singly_linked_list.head == None:
        return None

    # edge case: only one item in list, therefore is head, tail, and middle!
    # #Return the head node.
    if singly_linked_list.head.next == None:
        return singly_linked_list.head
    
    # cache the current last item you have iterated to at
    last = singly_linked_list.head
    # cache the current middle of your traversed list
    middle = singly_linked_list.head
    # create a counter
    i = 1

    # iterate until you reach the tail, at which point last.next() will be False
    while last.next == True:
        last = last.next
        i += 1
        if i % 2 == 1:
            middle = middle.next
    return middle
    





# if i % 2 = 1:
#     then middle equals old middle.next()

# # 1

# # 1


# # 1, 2

# # 1


# 1, 2, 3

# 2

# 1, 2, 3, 4

# 2

# 1, 2, 3, 4, 5

# 3

# 1, 2, 3, 4, 5, 6

# 3

# Second Class Guided Problem Specification:
# How do you reverse a singly linked list without recursion? You may not store the list, or it’s values, in another data structure.
