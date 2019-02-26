class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        print(self.storage)
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
        print(index)
        parent_index = max(0, ((index + 1)//2) - 1)  # round down
        print(self.storage)
        print(f'parent index {parent_index}')
        if self.storage[parent_index] < self.storage[index]:
            self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        path = []
        location = len(self.storage) - 1
        while location > 0:
            path.append(location)
            location = max(0, ((location + 1)//2) - 1)
        print(path)

        while len(path):
            sift_loc = 0
            swap_loc = path.pop(len(path) - 1)
            while self.storage[sift_loc] < self.storage[swap_loc]:
                self.storage[sift_loc], self.storage[swap_loc] = self.storage[swap_loc], self.storage[sift_loc]
                sift_loc = swap_loc
                try:
                    swap_loc = path.pop(len(path) - 1)
                except IndexError:
                    swap_loc = sift_loc
