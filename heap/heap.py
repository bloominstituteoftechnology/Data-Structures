class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # pass
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        # pass
        print('self.storage:', self.storage)
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # pass
        # print('value of index passed in:', index)
        # import math
        # import time

        # p = math.floor((index - 1)/ 2) if index > 1 else 0
        p = (index - 1) // 2
        current_value = self.storage[index]
        parent_value = self.storage[p]

        while index > 0:
            print('index:', index, 'p:', p)
            print('self.storage at buble up:', self.storage)
            if current_value > parent_value and p <= 0:
                self.storage[index] = parent_value
                parent_value = current_value
                index = p
                p = ((index - 1) // 2)
            else:
                break

            # print("walked through")
        # time.sleep(0.25)
        # p = math.floor((index - 1)/ 2) if index > 0 else 0
        # print('index:', index, 'p:', p)
        # print('self.storage at buble up:', self.storage)
        # current_value = self.storage[index]
        # parent_value = self.storage[p]

        # if current_value > parent_value:
        #   self.storage[index] = parent_value
        #   self.storage[p] = current_value
        #   self._bubble_up(p)

    def _sift_down(self, index):
        pass
        # first_child = self.storage[2 * index + 1 ]
        # second_child = self.storage[2 * index + 2 ]
        # while self.storage[index] < first_child or second_child:
        #   better_child = first_child >
