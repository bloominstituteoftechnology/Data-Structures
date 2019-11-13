import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

list = SinglyLinkedList()
list.insert_node(range(10))

print_singly_linked_list(list)

def get_mid(linkedList):
    node = linkedList.head
    counter = 0
    middle = linkedList.head
    while node:
        if counter > 1 and counter % 2 == 0:
            middle = middle.next
        counter += 1
        node = node.next
    return middle

print(get_mid(list).data)

node.head = node.tail
node.next = node.head
node.next = node.head
node.next = node.head