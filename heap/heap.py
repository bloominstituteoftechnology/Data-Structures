import math


class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        print("self.storage in insert", self.storage)
        self.size += 1
        print(self.size)
        print("self.storage in insert else", self.storage)
        if value > self.storage[0]:
            for i in self.storage:
                if i > self.storage[0]:
                    Heap._bubble_up(self, self.size - 1)
        else:
            for i in self.storage:
                Heap._bubble_up(self, self.size - 1)

    def delete(self):
        if self.size == 0:
            return None
        else:
            top = self.storage[1]
            self.storage[1] = self.storage[self.size]
            del self.storage[-1]
            self.size -= 1
            if self.size > 0:
                Heap._sift_down(self, 1)
            return top

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        print("index", self.storage[index])
        print("math.floor(index / 2)", self.storage[math.floor(index / 2)])
        if index > 1:
            while self.storage[index] > self.storage[math.floor(index / 2)]:
                temp = self.storage[math.floor(index / 2)]
                newindex = math.floor(index / 2)
                print("temp", temp)
                self.storage[math.floor(index / 2)] = self.storage[index]
                self.storage[index] = temp
                if self.storage[newindex] > self.storage[math.floor(newindex / 2)]:
                    Heap._bubble_up(self, newindex)


def _sift_down(self, index):
    if index * 2 + 1 <= self.size:
        if self.storage[index] < self.storage[index * 2]:
            if self.storage[index * 2] < self.storage[index * 2 + 1]:
                newindex = index * 2 + 1
                temp = self.storage[index * 2 + 1]
                self.storage[index * 2 + 1] = self.storage[index]
                self.storage[index] = temp
                if newindex * 2 + 1 <= self.size:
                    Heap._sift_down(self, newindex)
            elif self.storage[index * 2] > self.storage[index * 2 + 1]:
                newindex = index * 2
                temp = self.storage[index * 2]
                self.storage[index * 2] = self.storage
                self.storage[index] = self.storage[index * 2]
                if newindex * 2 <= self.size:
                    Heap._sift_down(self, newindex)
    elif index * 2 <= self.size:
        if self.storage[index] < self.storage[index * 2]:
            newindex = index * 2
            temp = self.storage[index * 2]
            self.storage[index * 2] = self.storage[index]
            self.storage[index] = temp
            if newindex * 2 <= self.size:
                Heap._sift_down(self, newindex)
    elif index + 2 <= self.size:
        if self.storage[index + 2] > self.storage[index + 1]:
            newindex = index + 2
            temp = self.storage[index + 2]
            self.storage[index + 2] = self.storage[index]
            self.storage[index] = temp
        if self.storage[index + 1] > self.storage[index + 1]:
            newindex = index + 1
            temp = self.storage[index + 1]
            self.storage[index + 1] = self.storage[index]
            self.storage[index] = temp
            if newindex + 1 <= self.size:
                Heap._sift_down(self, newindex)
    elif index + 1 <= self.size:
        newindex = index + 1
        temp = self.storage[index + 1]
        self.storage[index + 1] = self.storage[index]
        self.storage[index] = temp
        if newindex + 1 <= self.size:
            Heap._sift_down(self, newindex)


heap = Heap()
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)
heap.delete()
print("storage after insertions", heap.storage)
print("size after insertions and one delete", heap.size)

descending_order = []

# while heap.get_size() > 0:
#     descending_order.append(heap.delete())
#     print(descending_order)

