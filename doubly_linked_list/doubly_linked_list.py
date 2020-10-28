"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def delete(self):
        if self.prev:
            # self.next.prev = self.prev
            self.prev.next = self.next
        if self.next:
            # self.prev.next = self.next
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        """
            1. create new_node
            2. add to empty
            3. add to nonempty
        """
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        cur_node = self.head

        # print(f"node is: {cur_node.value} ")
        # print(f"node prev: {cur_node.next.next.value} ")

        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = cur_node.next
            cur_node.next.prev = cur_node.prev

        self.length -= 1
        return cur_node.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        cur_node = self.tail

        # print(f"node is: {cur_node.value} ")
        # print(f"node prev: {cur_node.prev.value} ")

        if self.tail is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = cur_node.prev
            cur_node.prev.next = cur_node.next

        self.length -= 1
        return cur_node.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        """
            1. delete()
            2. add_to_head()
        """
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        """
            1. dont need to return value
            2. do need to update heade, tail
        """
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:  # list has +2 nodes
            self.head = node.next
            node.delete()  # updating previous and next pointers
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # curNode = self.head

        # valueList = []

        # while True:
        #     if curNode is None:
        #         break
        #     valueList.append(curNode.value)
        #     curNode = curNode.next
        # return max(valueList)
        if self.head is None:
            return None
        cur_node = self.head
        max_value = self.head.value
        while cur_node:
            if cur_node.value > max_value:
                max_value = cur_node.value
            cur_node = cur_node.next
        return max_value

    def printList(self):
        if self.head is None:
            return "list is empty"
        currentNode = self.head
        ret_value = []
        while True:
            if currentNode is None:
                break
            ret_value.append(currentNode.value)
            currentNode = currentNode.next
        return ret_value

# # Test
myList = DoublyLinkedList()
myList.add_to_head(1)
myList.add_to_head(2)
myList.add_to_head(33)
myList.add_to_head(4)
myList.add_to_head(5)
myList.add_to_head(6)

myList.add_to_tail(20)


print(f"myList: {myList.printList()} ")

myList.remove_from_tail()

print(f"myList: {myList.printList()} ")

print(f"max value: {myList.get_max()} ")
