class BinarySearchTree:
	def __init__(self):
		self.max = 0
		self.size = 0
		self.root = None

	def insert(self, value):
		if(self.root == None):
			root = Node(value)
		else:
			self.insertCreateNode(self, self.root, vaule)
	
	def insertCreateNode(self, curr_node, value):
		if(value <= curr_node.value):
			if(curr_node.hasLeftChild()):
				self.insertCreateNode(self, curr_node.getLeftChild(), value)
			else:
				curr_node.setLeftChild(Node(value))
		elif(value > curr_node.value):
			if(curr_node.hasRightChild()):
				self.insertCreateNode(self, curr_node, value)
			else:
				curr_node.setRightChild(Node(value))

			
	def contains(self, target):
		curr_node = self.root
		if(target == curr_node.value):
			return True
		else:
			self.containsHelper(self, curr_node, target)
			
	def containsHelper(self, curr_node, target):
		if(target == curr_node):
			return True
		elif(curr_node.hasChild()):
			if(target < curr_node.value):
				self.containsHelper(self, curr_node.getLeftChild(), target)
			elif(target > curr_node.value):
				self.containsHelper(self, curr_node.getRightChild(), target)
		else:
			return False

	def getMax(self):
		if(self.root.hasRightChild() == False):
			return self.root.value
		else:
			return self.maxHelper(curr_node)

	def maxHelper(self, curr_node):
		if(curr_node.hasRightChild() == False):
			return curr_node.value
		else:
			self.maxHelper(curr_node.getRightChild())


class TreeNode:
	def __init__(self,value,left=None,right=None, parent=None):
			self.value = 0
			self.leftChild = left
			self.rightChild = right
			self.parent = parent
			self.root = False
	
	def hasChild(self):
		return True if(self.rightChild != None or self.leftChild != None) else False
	
	def hasLeftChild(self):
		return True if (self.getLeftChild() != None) else False

	def hasRightChild(self):
		return True if (self.getRightChild() != None) else False

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def setRightChild(self, node):
		self.rightChild = node

	def setLeftChild(self, node):
		self.leftChild = node

	def isRoot(self):
		return True if (self.root == True) else False

	def setAsRoot(self):
		if(self.isRoot == False): 
			self.isRoot = True