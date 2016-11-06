import heapq


class PriorityQueue:
    """
    A Priority Queue
    """
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        self.index += 1
        heapq.heappush(self.queue, (-priority, self.index, item))

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def print_q(self):
        for el in self.queue:
            print(el)




class Item:
    """
    Class to repr an Item
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name





q = PriorityQueue()
q.push(Item('Bob'), 32)
q.push(Item('San'), 2)
q.push(Item('Mark'), 22)
q.push(Item('David'), 12)

q.print_q()

print(q.pop())
print(q.pop())
print(q.pop())

q.print_q()

