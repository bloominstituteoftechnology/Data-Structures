class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,head,tail):
        self.head = head 
        self.tail = tail
        self.length = 0

    def add_to_head(self,data):
        newnode = Node(data)
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            newnode.next = self.head
            self.head = newnode

    def add_to_tail(self,data):
        newnode = Node(data)
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode
            self.length += 1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1

    def remove_head(self):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value

    def remove_tail(self):
        if self.length == 0:
            return None
        elif self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else: 
            value = self.tail.data
            currentnode = self.head
            while currentnode.next != self.tail:
                currentnode = currentnode.next
            self.tail = currentnode
            self.length -= 1
            return value

    def len(self):
        return self.length

    def view(self):
        list = []
        currentnode = self.head
        while currentnode != self.tail:
            list.append(str(currentnode.data))
            currentnode = currentnode.next
        list.append(str(currentnode.data))
        return '-->'.join(list)

LL = LinkedList(None,None)
LL.add_to_head(2)
LL.add_to_tail(4)
LL.add_to_tail(6)
print(LL.view())
LL.remove_head()
print(LL.view())
LL.remove_head()
print(LL.view())
LL.add_to_tail(5)
LL.add_to_tail(10)
LL.add_to_tail(15)
print(LL.view())
LL.add_to_tail(6)
print(LL.view())
LL.add_to_tail(6)
print(LL.view())