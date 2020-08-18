class Queue:
    '''
    Objective : To implement a queue using stacks.
    '''
    def __init__(self):
        '''
        Objective        :  To initialize an object of class Queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : None
        '''
        self.stack1 = []
        self.stack2 = []

    def Enqueue(self , ele):
        '''
        Objective        : To insert an element in queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
                             ele -> Element to be inserted
        Output           : None
        '''
        self.stack1.append(ele)

    def Dequeue(self):
        '''
        Objective        : To delete an element from queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : None
        '''
        if len(self.stack1) == 0 and len(self.stack2) == 0 :
            print('\nQUEUE IS EMPTY!!!.')
            return None
        else :
            if len(self.stack2) == 0:
                while len(self.stack1)!=0:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
                    
        

    def __str__(self):
        '''
        Objective        : To return string representation of an object of class Queue.
        Input Parameters :
        self(Implicit Parameter) -> Object of class Queue
        Output           : String
        '''
        queue = []
        if len(self.stack2)!=0:
            for i in range(len(self.stack2)-1,-1,-1):
                queue.append(self.stack2[i])
        if len(self.stack1)!=0:
            for i in range(0,len(self.stack1)):
                queue.append(self.stack1[i])
        if len(queue) == 0:return '\nQUEUE IS EMPTY !!'
        else:print('\nQUEUE :')
        return ' || '.join(str(x) for x in queue)

if __name__ == '__main__':
    q = Queue()
    q.Enqueue(13)
    q.Enqueue(56)
    q.Enqueue(78)
    print(q)
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.Dequeue())
    print(q)
    q.Enqueue(45)
    q.Enqueue(33)
    print(q)
    
        
        
            
        
