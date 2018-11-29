class Node:
    def __init__ (self, nodeValue = None):
        self.nodeValue=nodeValue
        self.leftNode=None
        self.rightNode=None

    def insert(self,data):
        if self.nodeValue:
            
            if data < self.nodeValue:
                if self.leftNode is None:
                    self.leftNode = Node(data)
                else:
                    self.leftNode.insert(data)
            
            elif data > self.nodeValue:
                if self.rightNode is None:
                    self.rightNode = Node(data)
                else:
                    self.rightNode.insert(data)
        else:
            self.nodeValue = data

    def printTree(self):
        if self.leftNode:
            self.leftNode.printTree()
        print(self.nodeValue)
        if self.rightNode:
            self.rightNode.printTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
#root.insert(3)

root.printTree()

        


