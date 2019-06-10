  #  Linear data structures
  #----------------------------------------------------------------------
    #  Queues => FIFO => First one In, First one Out
        #  => FIFO 
          #  => First one In, First one Out 
          #  => i.e. - line to ride a roller coaster, printer jobs
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
      #  => LIFO 
          #  => Last one In, First one Out 
          #  => i.e. - stack of plates
      #  lookup 
          #  => O(n)
      #  pop (remove last item) 
          #  => O(1)
      #  push (add an item to end of the stack) 
          #  => O(1)
      #  peek (view the top-most item in the stack)
          #  => O(1)
#----------------------------------------------------------------------

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = 

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    pass
