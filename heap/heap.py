class Heap:
    def __init__(self):
        self.storage = []

    def get_parent_index(self, index):
        if index == 0:
            return 0
        return (index-1) // 2

    def insert(self, value):
        self.storage.append(value)
        current_index = len(self.storage) - 1
        self._bubble_up(current_index)

    def delete(self):
        deleted_value = self.storage.pop(0)
        self._sift_down(0)
        return deleted_value

    def get_max(self):
      if self.get_size() is 0:
        return None
      return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = self.get_parent_index(index)
        parent_value = self.storage[parent_index]
        current_value = self.storage[index]
        if index is not 0 and parent_value < current_value:
          self.storage[index], self.storage[parent_index] = \
          self.storage[parent_index], self.storage[index]
          if parent_index is not 0:
            self._bubble_up(parent_index)
    def _sift_down(self, index):
        size = self.get_size()
        first_child_index = (2 * index) + 1
        second_child_index = (2 * index) + 2
        # if parent has child
        if first_child_index < size:
          parent_value = self.storage[index]
          first_child_value = self.storage[first_child_index]
          # if parent has 2 children
          if second_child_index < size:
            second_child_value = self.storage[second_child_index]
            if first_child_value >= second_child_value:
              if parent_value < first_child_value:
                self.storage[index], self.storage[first_child_index] = \
                first_child_value, parent_value
            elif parent_value < second_child_value:
              self.storage[index], self.storage[second_child_index] = \
              second_child_value, parent_value
            self._sift_down(index + 1)
          # else parent has only 1 child
          else:
            if parent_value < first_child_value:
              self.storage[index], self.storage[first_child_index] = \
              first_child_value, parent_value
            self._sift_down(index + 1)
