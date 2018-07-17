class Heap:
    def __init__(self):
        # storage starts with an unused 0 to make
        # integer division simpler later on
        self.storage = [0]
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        # print('\n', self.storage)
        self.size += 1
        valueIndex = len(self.storage) - 1
        # print('len', valueIndex + 1)
        # parentIndex = valueIndex // 2
        # parent = self.storage[parentIndex]
        self._bubble_up(valueIndex)

        print('\n', self.storage, '\n\n\n\n')

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        currentvalue = self.storage[index]
        parentIndex = index // 2
        parent = self.storage[parentIndex]
        while currentvalue > parent and parentIndex != 0:
            self.storage[index // 2] = currentvalue
            self.storage[index] = parent
            index = parentIndex
            currentvalue = self.storage[index]
            parentIndex = index // 2
            parent = self.storage[parentIndex]

    def _sift_down(self, index):
        pass

    def get_parent(self, currentPosition):
        return currentPosition // 2
