class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        return self._bubble_up(self.get_size() - 1)

    def delete(self):
        storage = self.storage
        storage[0], storage[self.get_size() - 1] = storage[self.get_size() - 1
                                                           ], storage[0]
        pop = storage.pop()
        self._sift_down(0)
        return pop

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        storage = self.storage
        if index == 0:
            return
        if storage[(index - 1)//2] > storage[index]:
            return
        elif storage[(index-1)//2] < storage[index]:
            storage[(index-1) //
                    2], storage[index] =\
                storage[index], storage[(index - 1)//2]
            return self._bubble_up((index - 1)//2)

    def _sift_down(self, index):
        storage = self.storage
        max_ch_id = None
        if index * 2 + 1 >= self.get_size():
            return
        elif index * 2 + 2 >= self.get_size():
            max_ch_id = index * 2 + 1
        elif storage[index * 2 + 1] > storage[index * 2 + 2]:
            max_ch_id = index * 2 + 1
        else:
            max_ch_id = index * 2 + 2

        if storage[index] < storage[max_ch_id]:
            storage[index], storage[max_ch_id] = storage[max_ch_id], storage[index]
            self._sift_down(max_ch_id)
        else:
            return
