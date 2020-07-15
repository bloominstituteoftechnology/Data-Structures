class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = None

    def traverse(self):
        # grab the first node
        current_node = self.head

        # keep going until you reach the end of the list:
        while current_node is not None:

            print(current_node.data)
            current_node = current_node.next_node

    def get_size_list(self):

        # define incrementer
        count = 0

        # grab the first node
        current_node = self.head

        # keep going until you reach the end of the list:
        while current_node is not None:

            count += 1
            current_node = current_node.next_node

        print("Count", count)

    def insert_beg(self, data):

        # define a new node
        new_node = Node(data)

        # set the next node equal to the old head
        new_node.next_node = self.head

        # Because it is the head, the previous pointer will point to nothing
        new_node.prev_node = None

        if self.head is not None:
            self.head.prev_node = new_node

        # update the head
        self.head = new_node


double_list = DoubleLinkedList()

double_list.insert_beg(90)
double_list.insert_beg(90)
double_list.insert_beg(90)
double_list.insert_beg(80)
double_list.insert_beg(70)

print('-'*100)
print('After Insertion')
print('-'*100)

double_list.traverse()

double_list.get_size_list()
