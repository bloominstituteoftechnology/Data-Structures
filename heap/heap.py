class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0 

  def insert(self, value):
    """ check if there is a item in the list already at index 0 
    If there is no item just add in the new item.  at this point  checks would be done on the first element to make decesion whether
    to peform other operations. it would seem that we need 3 items in the list before  really having to do major operations. 
    For example on the first element just add it in. on the second element  one comparison is it bigger or smaller than whats there 
    if its bigger insert it in the front  if it is smaller just put it in the back. on the third item now we do the same comparison has
    comparison when adding the second element. is it bigger than the first.  no  just add it in.    since it doesn't matter on the second
    level much.  After this point we would have insert at the back of the list  and then  bubble up accordingly.   
    or maybe its best to always bubble up and always put the item in the back and perform bubble up?  Is it worth it to do it any other way.
    as far as time compleixty it might be about the same. 
    """
    self.storage.append(value) # for two lines vs unknown it is worth it. Also readiability the _bubble_up(0) is also protected with _
    self.size += 1 
    if self.size > 1:
      self._bubble_up(self.size -1)

  def delete(self):
    """To delete I think what needs to happen is  i take the right most item. I believe this ccould be done easily with a pop()
       I now can set a varaible to equal the return of the pop.   I know can  self.storage[0] = popped  then call the  _sift_down()
    """
    self.size -= 1
    popped = self.storage.pop()
    self.storage[0] = popped
    self._sift_down(0) # should always been the 0 index no variable needed. 

    pass

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    """ index is the index of the element that will be moving up the heap
    keep bubbling the elemnt at the given index up the heap until it reaches a valid a valid spot """
    
    """ check if the elements parent's value is less than the current value """
    while (index -1) // 2 >= 0:
        if self.storage[(index -1)// 2] < self.storage[index]:
            self.sotriage [index], self.storage[(index-1)//2] = self.storage[(index - 1)//2], self.storage[index]
            #update the index to the parents so taht we continue moving up the heap 
        index = (index -1) // 2 

  def _sift_down(self, index):
    pass
    #similar but the cases are different change the formula plug checking higher priority and which two they need to swap with
