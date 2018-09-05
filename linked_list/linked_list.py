"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_to_tail(self, value):
		node = Node(value)		

		#If the head is empty, set the head and tail to new node
		if self.head == None:
			self.head = Node(value)
			self.tail = Node(value)
		
		#Else if head.next_node is None, now create a separate tail
		elif self.head.next_node == None:
			self.tail = node
			self.head.set_next(self.tail)
		
		#Now all other adds are to append to the tail
		else:
			current_tail = self.tail
			current_tail.set_next(node)
			self.tail = node

	def remove_head(self):
		pass

	def contains(self, value):

		#Check the head/tail for the value
		if self.head.get_value() == value or self.tail.get_value() == value:
			return True
		
		#Else while through the rest of the link checking each value
		else:
			#assume it's not found, init the contains var
			contains = False

			#Reference to the head as a starting point
			node = self.head
			
			#While we're not at the tail:
			while node.next_node != None:

				# Is the value here?	
				if node.get_value() == value:
					contains = True 
				
				#Set the next node (note making this an else, makes it an infinite loop!!!!!)
				node = node.get_next()

			return contains

	def get_max(self):
		pass



#Testing consecutive additions to tail and printing them out:
list = LinkedList()
print('\n append a 1')
list.add_to_tail(1)
print(list.head.get_value())

print('\n append a 9')
list.add_to_tail(9)
print(list.head.get_value())
print(list.head.get_next().get_value())

print('\n append a -34, and print them all out')
list.add_to_tail(-34)
print(list.head.get_value())
print(list.head.get_next().get_value())
print(list.head.get_next().get_next().get_value())

print('\n check if it has 10')
print(list.contains(9))