class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = len(self.storage) - 1
        self._bubble_up(index)

    def delete(self):
        root = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        self._sift_down(0)
        self.storage.pop()
        return root


    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index -1) // 2 >= 0:
            if(self.storage[index] > self.storage[(index -1)//2]):
                self.storage[index], self.storage[(index -1)//2] = self.storage[(index -1)//2],self.storage[index] 
            index = (index -1)//2


    def _sift_down(self, index):
        while(2*index + 1 <= len(self.storage)-1):
            max = self.max_index(index);
            if(self.storage[index] < self.storage[max]):
                self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
            index = max

    def max_index(self, index):
        if (2*index + 2 > len(self.storage) -1):
            return index*2+1
        else:
            if(self.storage[index*2 +1]> self.storage[index*2 +2]):
                return index*2+1
            else:
                return index*2+2

    