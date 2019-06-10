  #  Linear data structures
  #----------------------------------------------------------------------
    #  Queues => FIFO => First one In, First one Out
        #  FIFO 
          #  => First one In, First one Out 
          #  => i.e. - line to ride a roller coaster, printer jobs
        #  Can be built with:
            #  => Arrays
            #  => Linked Lists
        #  Methods
            #  lookup 
                #  => O(n)
            #  enqueue (add an item to the BACK of the queue) 
                #  => O(1)
            #  dequeue (remove an item from the FRONT of the queue) 
                #  => O(1)
            #  peek (view the FRONT-most item in the queue)
                #  => O(1)
#----------------------------------------------------------------------
  #  Stacks 
      #  LIFO 
          #  => Last one In, First one Out 
              #  => has a "top" and a "bottom"
              #  => i.e. - stack of plates
      # Can be built with:
          #  => Arrays
          #  => Linked Lists
      #  Methods
          #  lookup 
              #  => O(n)
          #  pop (remove last item) 
              #  => O(1)
          #  push (add an item to end of the stack) 
              #  => O(1)
          #  peek (view the TOP-most item in the stack)
              #  => O(1)
#----------------------------------------------------------------------
#   What are the pros and cons to using an array as the data structure 
#   for building a queue?
    #   Pros
        #   Cache Locality => faster when accessing items from memory
        #     because items are right next to each other.
    #   Cons
        #   It's very inefficient. If you .shift() an item from the 
        #     beginning of an array, you'd have to shift the remaining
        #     indexes.
        #   Static/dynamic array will have certain amount of memory, which
        #     will have to double up that memory to create more space for
        #     new items.
        
#   What are the pros and cons to using a linked list as the data structure 
#   for building a queue?
    #   Pros
        #   Uses dynamic memory => allows us to keep adding things to the list
        #   If item is removed from list, items don't need to be shifted due to 
        #     indexing.
    #   Cons
        #   Items are scattered all over memory.
        #   Requires more memory to store items because of the arrows we need.
        
#   ***WINNER (for building a queue)*** => Linked Lists

#  Creates a Node class to store individual entries for the queue
class Node:
    def __init__(self, value=None, next_node=None):
       self.value = value
       self.next_node = next_node
 
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            self.tail = self.tail.next_node
        self.size += 1
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return to_return 
          
    def len(self):
        return self.size