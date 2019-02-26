class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        top_value = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        del self.storage[len(self.storage) - 1]
        if len(self.storage):
            self._sift_down(0)
        return top_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = max(0, ((index + 1)//2) - 1)  # round down
        if self.storage[parent_index] < self.storage[index]:
            self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        pointer = index
        left = pointer * 2
        right = pointer * 2 + 1

        finished = False

        while not finished:
            try:
                if self.storage[pointer] < self.storage[left] or self.storage[pointer] < self.storage[right]:
                    if self.storage[left] > self.storage[right]:
                        self.storage[pointer], self.storage[left] = self.storage[left], self.storage[pointer]
                        pointer = left
                        left = pointer * 2
                        right = pointer * 2 + 1
                    else:
                        self.storage[pointer], self.storage[right] = self.storage[right], self.storage[pointer]
                        pointer = right
                        left = pointer * 2
                        right = pointer * 2 + 1
                else:
                    finished = True
            except IndexError:
                try:
                    if self.storage[pointer] < self.storage[left]:
                        self.storage[pointer], self.storage[left] = self.storage[left], self.storage[pointer]
                        pointer = left
                        finished = True
                    else:
                        finished = True
                except IndexError:
                    finished = True

        for index, val in enumerate(self.storage):
            self._bubble_up(index)
