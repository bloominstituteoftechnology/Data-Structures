class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        heap_top = self.storage[0]
        heap_end = self.storage[-1]
        if (self.get_size()>1):
          self.storage = [heap_end] + self.storage[1:-1]
          self._sift_down(0)
        else:
          self.storage=[]
        return heap_top

    def get_max(self):
        if not self.storage:
            return None
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index-1)//2>=0:

            if self.storage[(index-1)//2] < self.storage[index]:
            #swap values
                self.storage[index], self.storage[(index-1)//2]=self.storage[(index-1)//2], self.storage[index]
        
            index=(index-1)//2 #update the index to parent's index to keep moving up

    def _sift_down(self, index):
        while True:
            left_index = 2*index+1
            right_index = 2*index+2
            temp_index = None

            if (left_index < self.get_size()):
                if self.storage[left_index] > self.storage[index]:
                    temp_index = left_index

            if (right_index < self.get_size()):
                if (temp_index == None and self.storage[right_index] > self.storage[index]) or (temp_index != None and self.storage[right_index] > self.storage[left_index]):
                    temp_index = right_index

            if not temp_index:
                break

            self.storage[index], self.storage[temp_index] = self.storage[temp_index], self.storage[index]
            index = temp_index

