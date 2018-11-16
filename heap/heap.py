class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # print(f"before: {self.storage}")
        if len(self.storage) > 1:  # if there's at least 2 storage items
            root_value = self.storage[0]  # store the root node for return statement
            self.storage[0] = self.storage[
                -1
            ]  # make the root node the last item in array
            self.storage.pop()  # pop off the last item in array, effectively deleting it
            self._sift_down(0)  # sift the root node downwards
            # print(f"after: {self.storage}")
            return root_value  # return root node per tests
        else:
            deleted_value = self.storage[0]
            self.storage.pop()
            return deleted_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:  # while there's a parent node, keep running
            if (
                self.storage[index] > self.storage[(index - 1) // 2]
            ):  # if the current value is larger than parent value
                self.storage[index], self.storage[
                    (index - 1) // 2
                ] = (  # switch them and continue the while loop until no more parent node
                    self.storage[(index - 1) // 2],
                    self.storage[index],
                )
            else:
                break

    def _sift_down(self, index):
        while (
            index * 2 + 1 < len(self.storage) - 1
        ):  # while left child is not out of bounds
            mc = self._max_child(index)
            if (
                self.storage[index] < self.storage[mc]
            ):  # if current child is less than largest child from left or right, swap the values
                self.storage[index], self.storage[mc] = (
                    self.storage[mc],
                    self.storage[index],
                )
                index = (
                    mc
                )  # now set new index as next largest child so while loop can keep running

    def _max_child(self, index):
        if (
            index * 2 + 2 > len(self.storage) - 1
        ):  # if the right child is out of bounds, return the left
            return index * 2 + 1
        else:
            if (
                self.storage[index * 2 + 1] > self.storage[index * 2 + 2]
            ):  # if left child is larger than right child, return left child
                return index * 2 + 1
            else:  # vice versa
                return index * 2 + 2
