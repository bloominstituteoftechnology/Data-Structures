class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        index = len(self.storage)
        self.storage.append(value)
        self._bubble_up(index)

    def delete(self):
        deleted = self.storage.pop(0)
        if self.storage:
            temp = self.storage.pop()
            self.storage.insert(0, temp)
            self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        n = self.get_size()
        while index < n - 1:
            left = 2*index + 1
            right = 2*index + 2
            if left < n and right < n:
                if self.storage[left] >= self.storage[right]:
                    child = left
                else:
                    child = right
            elif left < n:
                child = left
            else:
                break
            if self.storage[child] > self.storage[index]:
                self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
                index = child
            else:
                break
