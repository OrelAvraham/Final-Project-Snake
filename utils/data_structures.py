import heapq


class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


class Queue:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.insert(0, val)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.init = False

    def push(self, item, priority):
        if not self.init:
            self.init = True
            try:
                item < item
            except:
                item.__class__.__lt__ = lambda x, y: (True)

        pair = (priority, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        return len(self.heap) == 0


# class PriorityQueue:
#     """
#     Assumption, the data is organized in tuples (or other iterables) in this order (value, priority)
#     so element[0] = value and element[1] = priority
#     value is a tuple itself with this structure (point, path, ,cost)
#     """
#
#     def __init__(self):
#         self.list = []
#
#     def push(self, val, priority):
#
#         if len(self.list) == 0:
#             self.list.append((val, priority))
#         else:
#             for (i, e) in enumerate(self.list):
#                 if priority < e[1]:
#                     self.list.insert(i, (val, priority))
#                     return
#
#     def pop(self):
#         return self.list.pop()[0]
#
#     def is_empty(self):
#         return len(self.list) == 0
