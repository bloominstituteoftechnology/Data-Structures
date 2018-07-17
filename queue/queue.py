import sys
sys.path.extend('../linked_list')
#sys.path.append('C:\Users\HPENVY\Data-Structures\linked_list')
from linked_list.linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()
    #https://lambdaschoolstudents.slack.com/archives/CBQ2B0V7Y/p1531774652000259
    #self.storage = []

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size +=1
  

  def dequeue(self):
    if self.size == 0:
      return None
    
    result= self.storage.remove_head()
    self.size -=1
    return result


  def len(self):
    return self.size
  '''
  def enqueue(self, item):
    self.storage.append(item)
    self.size=len(self.storage)
  

  def dequeue(self):
     if self.size > 0:
       element = self.storage.pop(0)
       self.size=len(self.storage)
       return element
     else:
       return None

  def len(self):
    return len(self.storage)


new_queue=Queue()
new_queue.enqueue(2)
print(new_queue.storage)
'''
