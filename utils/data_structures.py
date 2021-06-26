import heapq


class Stack:
    # Stack class - Uses a list to store the data and create the illusion of stack
    def __init__(self):
        self.list = []

    def push(self, val):
        # pushes a value to the stack (to the top)
        self.list.append(val)

    def pop(self):
        # pops a value out of the stack (from the top)
        return self.list.pop()

    def is_empty(self):
        # Checks if the stack is empty
        return len(self.list) == 0


class Queue:
    # Queue Class - Uses a list to store the data and create the illusion of queue
    def __init__(self):
        self.list = []

    def push(self, val):
        # pushes value to the queue (to the bottom)
        self.list.insert(0, val)

    def pop(self):
        # pops value form the queue (from the top)
        return self.list.pop()

    def is_empty(self):
        # Checks if the queue is wmpty
        return len(self.list) == 0


class PriorityQueue:
    # Priority queue - Uses list and the heapq module to create the illusion of priority queue
    def __init__(self):
        self.heap = []
        self.init = False

    def push(self, item, priority):
        # Push value to its place in the priority queue
        if not self.init:
            self.init = True

            # Checking if the object is comparable, if not make it
            try:
                item < item
            except:
                item.__class__.__lt__ = lambda x, y: (True)

        # The push itself
        pair = (priority, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        # Pop value form the priority queue
        (priority, item) = heapq.heappop(self.heap)
        return item

    def is_empty(self):
        # Checks if the priority queue is empty
        return len(self.heap) == 0

