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

        # print('\n', self.storage, '\n\n\n\n')

    def delete(self):
        print('\n\nDelete START\n', self.storage)
        if len(self.storage) == 1:
            print('\nDelete END\n', self.storage, '\n\n\n')
            return None

        firstItem = self.get_max()

        if len(self.storage) == 2:
            self.storage.pop()
            self.size -= 1
            print('\nDelete END\n', self.storage, '\n\n\n')
            return firstItem

        lastIndex = len(self.storage) - 1
        lastItem = self.storage[lastIndex]
        # swap values into the 'storage'
        self.swapValues(1, lastIndex)
        self.storage.pop()
        self.size -= 1

        self._sift_down(1)

        print('\nDelete END\n', self.storage, '\n\n\n')
        return firstItem

    def get_max(self):
        return self.storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        currentvalue = self.storage[index]
        parentIndex = index // 2
        parent = self.storage[parentIndex]

        # OPTION 1
        # while currentvalue > parent and parentIndex != 0:
        #     self.storage[index // 2] = currentvalue
        #     self.storage[index] = parent
        #     index = parentIndex
        #     currentvalue = self.storage[index]
        #     parentIndex = index // 2
        #     parent = self.storage[parentIndex]

        # OPTION 2
        if currentvalue > parent and parentIndex != 0:
            self.swapValues(parentIndex, index)
            self._bubble_up(parentIndex)

    def _sift_down(self, index):
        print('\n\nsift_down')
        print(self.storage)
        storageLen = len(self.storage)
        leftIndex = 2 * index
        rightIndex = (2 * index) + 1
        currentValue = self.storage[index]

        if leftIndex < storageLen:  # if LeftIndex is a valid index
            if rightIndex >= storageLen:  # if RightIndex is out the bounds of the Storage-Array
                if currentValue < self.storage[leftIndex]:
                    self.swapValues(index, leftIndex)
                    self._sift_down(leftIndex)
            elif rightIndex < storageLen:  # if RightIndex is a valid index
                leftValue = self.storage[leftIndex]
                rightValue = self.storage[rightIndex]

                if currentValue >= leftValue:
                    if currentValue < rightValue:
                        self.swapValues(index, rightIndex)
                        self._sift_down(rightIndex)
                if currentValue < leftValue:
                    if currentValue >= rightValue:
                        self.swapValues(index, leftIndex)
                        self._sift_down(leftIndex)
                    elif currentValue < rightValue:
                        childs = {
                            leftValue: leftIndex,
                            rightValue: rightIndex,
                        }
                        maxChildvalue = max(leftValue, rightValue)
                        print('maxChildvalue', maxChildvalue)
                        print('childs[maxChildvalue]', childs[maxChildvalue])
                        self.swapValues(
                            index, childs[maxChildvalue])
                        self._sift_down(childs[maxChildvalue])

    def get_parent(self, currentPosition):
        return currentPosition // 2

    def swapValues(self, parentIndex, childIndex):
        currentValue = self.storage[parentIndex]
        self.storage[parentIndex] = self.storage[childIndex]
        self.storage[childIndex] = currentValue
