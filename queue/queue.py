"""
Author: Tony Code
"""

class Queue:
    """
    A basic data structure that obey the rule "First In First Out"
    """

    
    def __init__(self, maxsize = 10):
        self.q = []
        self.maxsize = maxsize

    def __str__(self):
        return str(self.q)

    def empty(self):
        return not bool(self.q)

    def size(self):
        return len(self.q)
    
    def full(self):
        return len(self.q) == self.maxsize

    def push(self, e):
        if self.full():
            raise QueueOverflowError
        self.q.append(e)

    def pop(self):
        if self.empty():
            raise IndexError("pop from an empty queue")
        return self.q.pop(0)

    def front(self):
        if self.q:
            return self.q[0]

    def back(self):
        if self.q:
            return self.q[-1]

class QueueOverflowError(BaseException):
    pass

    