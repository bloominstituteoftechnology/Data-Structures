class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if not self.value:
            self.value = value
        else:
            pointer = self
            finished = False
            while not finished:
                if pointer.value == value:
                    finished = True
                elif pointer.value > value:
                    if pointer.left:
                        pointer = pointer.left
                    else:
                        pointer.left = Node(value)
                        finished = True
                else:
                    if pointer.right:
                        pointer = pointer.right
                    else:
                        pointer.right = Node(value)
                        finished = True

    def contains(self, target):
        pointer = self
        while True:
            if not pointer:
                return False
            if pointer.value == target:
                return True
            elif pointer.value > target:
                pointer = pointer.left
            else:
                pointer = pointer.right

    def get_max(self):
        pointer = self
        while pointer.right:
            pointer = pointer.right
        return pointer.value
