class Node:
    def __init__(self, nodeValue = None):
        self.nodeValue=nodeValue
        self.nextNode=None

class LinkedList:
    def __init__(self):
        self.headNode = None

    def printAllNodes(self):
        currentNode = self.headNode
        while currentNode is not None:
            print ("current node:",currentNode.nodeValue)
            currentNode = currentNode.nextNode

#create 4 nodes:
node4 = Node('Node 4')
node3 = Node('Node 3')
node3.nextNode = node4
node2 = Node('Node 2')
node2.nextNode = node3
node1 = Node('Node 1')
node1.nextNode = node2

list = LinkedList()
list.headNode=node1
list.printAllNodes()