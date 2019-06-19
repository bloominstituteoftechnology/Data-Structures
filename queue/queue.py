class Queue:
	def __init__(self):
		self.size = 0
	  # what data structure should we
	  # use to store queue elements?
		self.storage = Linked_List()

	def enqueue(self, item):
		# if no value in the queue add head
		if self.storage.head == None:
			value = Node(item)
			self.storage.change_head(value)
			self.size =+ 1
		else:
			self.storage.change_tail(item)
			self.size += 1
		#add new node to linked list
		#change tail to new node

	def dequeue(self):
		if self.storage.head == None:
			return None
		else:
			removed_node = Node(self.storage.head.get_value())
			self.storage.change_head()
			self.size -= 1
			return removed_node.get_value()
			
			

		#remove first node 
		#move head to next node

	def len(self):
		return self.size

	#que FIFO   <-- removing 1<-- adding
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
	
	def set_value(self, new_value):
		self.value = new_value

class Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None

	def change_head(self, node=None):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			temp = self.head.get_next()
			self.head = temp
			
			

	def change_tail(self, node):
		value = Node(node)
		self.tail.next_node = value
		value = self.tail


# items_queue = Queue()
# print(items_queue.len())
# items_queue.enqueue(1)
# items_queue.enqueue(2)
# print(items_queue.len())

