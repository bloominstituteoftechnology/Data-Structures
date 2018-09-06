class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # add value then buble up
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        max = self.storage[0]
        end = self.storage[-1]
        if (self.get_size()>1):
          self.storage = [end] + self.storage[1:-1]
          self._sift_down(0)
        else:
          self.storage=[]
        return max

    def get_max(self):
        if not self.storage:
            return None
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        node_index = index
        while node_index > 0:
            parent_index = (node_index-1)//2
            if self.storage[node_index] <= self.storage[parent_index]:
                break
            self.storage[node_index], self.storage[parent_index] = self.storage[parent_index], self.storage[node_index]
            node_index = parent_index

    def _sift_down(self, index):
        node_idx = index
        while True:
            left_idx = 2*node_idx+1
            right_idx = 2*node_idx+2
            swap_index = None

            if (left_idx < self.get_size()):
                if self.storage[left_idx] > self.storage[node_idx]:
                    swap_index = left_idx

            if (right_idx < self.get_size()):
                if (swap_index == None and self.storage[right_idx] > self.storage[node_idx]) or (swap_index != None and self.storage[right_idx] > self.storage[left_idx]):
                    swap_index = right_idx

            if not swap_index:
                break

            self.storage[node_idx], self.storage[swap_index] = self.storage[swap_index], self.storage[node_idx]
            node_idx = swap_index
        
        ''' === Recursive solution ===
        leftchild = index * 2 + 1
        rightchild = index * 2 + 2
        newindex = index

        if leftchild <= len(self.storage) -1:
            left_child_val = self.storage[leftchild]
            if left_child_val > self.storage[newindex]:
                newindex = leftchild
        if rightchild <= len(self.storage) -1:
            right_child_val = self.storage[rightchild]
            if right_child_val > self.storage[newindex]:
                newindex = rightchild
        if newindex is not index:
            self.storage[index], self.storage[newindex] = self.storage[newindex], self.storage[index]
            self._sift_down(newindex)
      '''
        
