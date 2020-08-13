class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # inserts at the beginning of the linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_end(self, data):
        # Check if head is empty
        if self.head is None:
            # If the head empty,
            # set the head to a new node with the incoming data.
            self.head = Node(data, None)
            return

        # If the head isn't empty,
        # iterate through the Linked List and add data to the end.
        itr = self.head
        while itr.next:
            # If itr.next has some value that means we're not at the end
            itr = itr.next
            # When itr.next becomes null,
            # we've reached the end of the Linked List
        itr.next = Node(data, None)

    # Removes all current values and inserts a data list
    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        # Error catching
        if index < 0 or index >= self.get_length():
            raise Exception("Invaild index")

        # If removing head,
        # set head to point to the next element
        if index == 0:
            self.head = self.head.next
            return

        # Removing anything besides the head
        # Manually keep track of each iteration
        count = 0

        # Iterate through the linked list
        itr = self.head
        while itr:
            # We have to find the element before the index to be removed..
            if count == index - 1:
                # Set the pointer to the element after the removed index
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        # Iterate through the LL
        itr = self.head
        while itr:
            # Find the data_after node
            if itr.data == data_after:
                # Once the node is found,
                # node.data = data_to_insert, node.next = the current iteration's next value
                node = Node(data_to_insert, itr.next)
                # set the current iteration's next value to be the current node
                itr.next = node
                break

            if itr.next == None:
                raise Exception('Data not found.')
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        # Remove first node that contains data
        # Iterate through the LL
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
            itr = itr.next
            count += 1

    # def remove_by_value(self, data):
    #     if self.head is None:
    #         return
    #
    #     if self.head.data == data:
    #         self.head = self.head.next
    #         return
    #
    #     itr = self.head
    #     while itr.next:
    #         if itr.next.data == data:
    #             itr.next = itr.next.next
    #             break
    #         itr = itr.next

if __name__ == '__main__':

    # ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(79)
    # ll.insert_values([1,2,3,4,5,6])
    # ll.remove_at(2)
    # ll.print()
    # ll.insert_at(6, 7)
    # ll.print()

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
