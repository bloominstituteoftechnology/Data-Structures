# UPER
# How do you find and return the middle node of a singly linked list in one pass?
# You do not have access to the length of the list.
# If the list is even, you should return the first of the two “middle” nodes.
# You may not store the nodes in another data structure.
# ONLY ACCESS TO HEAD NODE

# PLAN
# COUNTER VARIABLE, EACH TIME SOMETHING ADDED TO LINK LIST
# COUNTER .... BELOW
# IF EVEN :
#    / 2
# ELSE:
#    // 2 +1
#
nums = [0, 1, 2, 3, 4, 5, 6]
# EXECUTE

def middleNum(arr):
    counter = 0
    for num in nums:
        counter += 1
    if counter % 2 == 0:
        return print(nums[int(counter / 2 - 1)])

    else:
        return print(nums[counter // 2])


middleNum(nums)

def middleNum2(arr):
    current_head = arr.head
    slow_pointer = current_head
    fast_pointer = current_head

    while fast_pointer.next.next:
        slow_pointer.next

        return print(slow_pointer)

middleNum2(nums)
# list node class
#
# def findLLMid2(singleLinkList):
#     currentNode = singleLinkList.head
#     middleNode = currentNode
# 	currentNode = currentNode.next.next
# 	while currentNode is not None:
# 		middleNode = middleNode.next
# 		currentNode = currentNode.next.next
# 	return middleNode
#


# REVERSE SINGLE LINKED LIST IN ONE PASS

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

class SingleLinkedList:
    def __init__(self, node=None):
        self.length = 1 if node is not Node else 0

        def add_to_head(self, value):
            new_node = Node(value)








# RECURSION

"""Reverse a string
1. given string 'string'
2. return the string but in reverse order
"""


# base case
# new array?
# while loop
# while (what?)
# "this is our string"
# counter


# string = "output"

# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# take the last letter of what we got passed and add it to the beginning
# 'output'
# ...
# 'toutpu'


def reverse(string):
    if len(string) == 0:
        return string
    else:
        print(string)
        return reverse(string[1:]) + string[0]
    # output = []
    # while counter > 0:
    #     output.append(string[counter -1])
    #     print("".join(output))
    #     counter -=1


# a = str(input("Enter string: "))
print(reverse("ab cde"))
# print("".join(output))