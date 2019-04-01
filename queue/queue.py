# class Queue:
#     def __init__(self):
#         self.size = 0
#         # what data structure should we
#         # use to store queue elements?
#         self.storage = list()

#     def enqueue(self, item):
#         if item not in self.storage:
#             self.storage.insert(self.size, item)
#             # self.size += 1

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()
#             # self.size -= 1
#         else:
#             return None

#     def len(self):
#         return len(self.storage)


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = list()

    def enqueue(self, item):

        self.storage.insert(0, item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:

            self.size -= 1
            return self.storage.pop()
        return None

    def len(self):
        return self.size
