class Heap:
    def __init__(self):
      self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)
        print(self.storage)

    def delete(self):
        value = self.storage.pop(0)
        if self.storage:
            temp = self.storage.pop()
            self.storage.insert(0, temp)
            self._sift_down(0)
        return value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
      # 1. Check to see if the index is greater than zero
          # 2. Grab parent index
          # 3. Check if current value is greater than or less than parent value
          #     a. If current is greater than
          #     b. Swap
          # 4. If current is lesser than parent
          #     a. Leave it alone - break
        while index > 0:
            p = (index - 1) // 2

            if self.storage[index] > self.storage[p]:
                  #swap them
                self.storage[index], self.storage[p] = self.storage[p], self.storage[index]
                index = p #Updating your new index
            else:
                break #stop bubbling up, break out of loop

    def _sift_down(self, index): #essentially opposite of bubble up
        x = self.get_size()
        while index < x - 1:
            l = 2 * index + 1
            r = 2 * index + 2
            if l < x and r < x:
                if self.storage[l] >= self.storage[r]:
                    child = l
                else:
                    child = r
            elif l < x:
                child = l
            else:
                break
            if self.storage[child] > self.storage[index]:
                self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
                index = child
            else:
                break

