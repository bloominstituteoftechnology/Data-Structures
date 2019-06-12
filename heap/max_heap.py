# import s.s
from s import s as stack

class Heap:
    def __init__(self):
        # print('comparator is None:', comparator is None)
        self.Storage = stack([None])
        self.comparator = lambda x,y: x > y
        # print('comparer(3,2)', self.comparator(3,2))
        self.size = 0
        self.is_max = (self.comparator(1,2) == False)
        # print('is_max', self.is_max)

    @property
    def storage(self):
        return list(self.Storage)[1:]    

    def get_max(self):
        return self.Storage[1]

    def swappable(self, parent, child):
        # print('swappable', parent, child)
        return not self.comparator(parent, child)

    def is_parent(self, parent, child):
        return max(parent, child) if self.is_max else min(parent,child)

    def insert(self, value):
        # print('insert:', value)
        # print('input Storage', self.Storage)
        self.Storage.push(value)
        parent_index = self.get_size() // 2
        if parent_index == 0:
            if self.get_size() > 0:
                self._bubble_up(0) # for test_bubble_up only, with only 1 item nothing to bubble up
            # print('no while parent_index = 0 output Storage', self.Storage)    
            return
        val_index = self.get_size()
        while self.swappable(self.Storage[parent_index], value):
            # print('swappable', self.Storage[parent_index], value)
            self._bubble_up(val_index)
            val_index = parent_index
            parent_index = parent_index // 2
            if parent_index == 0:
                # print('while parent_index == 0 output Storage', self.Storage)
                return
        # print('eof output Storage', self.Storage)

    def delete(self): # aka poll
        if self.get_size() == 0:
            return None
        # print('input delete storage', self.Storage)            
        s1 = self.Storage[1]
        delete_value = self.Storage.pop()
        if self.get_size() > 0:
            self.Storage[1] = delete_value
            # print('delete sifting down:', delete_value)
            # print(self.Storage)
            self._sift_down(1)
        #     print('after delete sift down storage', self.Storage)
        # print('deleting:', s1)
        # print('after delete storage', self.Storage)
        return s1

    def get_priority(self):
        return self.Storage[1]

    def get_size(self):
        return len(self.Storage) - 1

    def _bubble_up(self, index):
        temp = self.Storage[index // 2]
        self.Storage[index // 2] = self.Storage[index]
        self.Storage[index] = temp

    def _sift_down(self, index):
        left = self.Storage[index * 2] if index * 2 <= self.get_size() else None
        right = self.Storage[index * 2 + 1] if index * 2 + 1 <= self.get_size() else None
        m = None
        if right is None:
            m = left
            if left is None:
                return
        else:
            m = self.is_parent(left, right)
        if self.swappable(self.Storage[index], m):
            sift_index = None
            if (right is None) or (not self.swappable(left, right)):
                self._bubble_up(index * 2)
                sift_index = index * 2
            else:
                self._bubble_up(index * 2 + 1)
                sift_index = index * 2 + 1
            self._sift_down(sift_index)
        return
