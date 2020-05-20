"""
Author: Tony Code
"""

class stack:
    """
    A basic data structure that obey the rule "First In Last Out"
    """

    
    def __init__(self, maxsize = 10):
        self.s = []
        self.maxsize = maxsize

    def __str__(self):
        return str(self.s)

    def empty(self):
        return not bool(self.s)

    def size(self):
        return len(self.s)
    
    def full(self):
        return len(self.s) == self.maxsize

    def push(self, e):
        if self.full():
            raise StackOverflowError
        self.s.append(e)

    def pop(self):
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.s.pop()

    def top(self):
        if self.s:
            return self.s[-1]

class StackOverflowError(BaseException):
    pass

    
