from pennant import Pennant

"""

"""
class Bag:
    def __init__(self):
        self.spine = [None for i in range(10)]
        self.count = 0

    def add(self, value):
        new_pennant = Pennant(value)
        cur_index = 0

        while self.spine[cur_index]:
            if cur_index > len(self.spine) - 1:
                self.spine.append(None)
                break
            combined = new_pennant.combine(self.spine[cur_index])
            self.spine[cur_index] = None
            cur_index += 1

        self.spine[cur_index] = new_pennant
