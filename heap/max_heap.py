class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # 1. Check to see if the index is greater than zero
        # 2. Grab parent index
        # 3. Check if current value is greater than or less than parent value
        #     a. If current is greater than
        #     b. Swap
        # 4. If current is lesser than parent
        #     a. Leave it alone - break
        while index > 0:
            parent = (index - 1) // 2

            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent #Updating your new index
            else:
                break

  def _sift_down(self, index):
    pass
