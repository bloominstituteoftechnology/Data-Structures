#from datastructures.linked_list import LinkedList
#sys.path.insert(0, '/Users/Ivan/Documents/iOS Development/Lambda iOS/Week 26 - Data Structures/Data-Structures/linked_list.py')
#sys.path.append('/Users/Ivan/Documents/iOS Development/Lambda iOS/Week 26 - Data Structures/Data-Structures/linked_list.py')
#from Users.Ivan.Documents.iOS
#FINALLY!!!!!!
import sys
sys.path.append('/Users/Ivan/Documents/iOS Development/Lambda iOS/Week 26 - Data Structures/Data-Structures')
from linked_list import LinkedList



class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    item = self.storage.remove_head()
    if self.size > 0:
      self.size -= 1
    return item

  def len(self):
    return self.size
