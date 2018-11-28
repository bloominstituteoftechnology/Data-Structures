class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.headNode = None

    def printList(self):
        currentNode = self.headNode
        while currentNode is not None:
            print(currentNode.dataVal)
            currentNode = currentNode.nextNode

list = LinkedList()
list.headNode = Node('First Node')
node2=Node('Second Node')
node3=Node('Third Node')
node4=Node('Fourth Node')
node3.nextNode=node4
node2.nextNode=node3
list.headNode.nextNode=node2

list.printList()

