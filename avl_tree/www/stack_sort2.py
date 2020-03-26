
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.value)


    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next


    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
        curr_node = self.head
        print(curr_node)
        while curr_node.next is not None:
            
            curr_node = curr_node.next
            print(curr_node)

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # this is first element in the list
        if not self.head and not self.tail :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
    
        max_value = self.head.value
        current = self.head

        while current: # while there is a current index, loop thru the array
            if current.value > max_value: # compare if current value is greater than max value
                max_value = current.value # if it is, we want to set the max value to current value

            current = current.next # increment

        return max_value


class Stack:
    def __init__(self):
        self.size = 0
        self.dbly_list = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        self.dbly_list.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.dbly_list.remove_from_head()

    def len(self):
        return self.size

    def peek(self):
      return self.dbly_list.head.value

my_stack = Stack()

my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
my_stack.push(2)
my_stack.push(4)

tmpStack = Stack() 
def sortStack ( stack ): 
	while stack.size == None: 
		# pop out the first element 
	    tmp = stack.head
	    Stack.pop(stack) 

		# while temporary stack is not 
		# empty and top of stack is 
		# greater than temp 
	    while tmpStack.size == None and int(tmpStack.head) > int(tmp): 
			
		# pop from temporary stack and 
		# push it to the input stack 
		    Stack.push(stack,tmpStack.head) 
		    Stack.pop(tmpStack) 
            # push temp in tempory of stack 
        Stack.push(tmpStack,tmp)  
    
        return tmpStack 
sortStack(my_stack)