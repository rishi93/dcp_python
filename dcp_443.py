"""
Daily Coding Problem - Day 443

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        try:
            val = self.stack.pop()
            return val
        except IndexError:
            return None
    def display(self):
        print(self.stack)

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, val):
        other_val = self.stack2.pop()
        while other_val:
            self.stack1.push(other_val)
            other_val = self.stack2.pop()
        self.stack1.push(val)
    
    def dequeue(self):
        other_val = self.stack1.pop()
        while other_val:
            self.stack2.push(other_val)
            other_val = self.stack1.pop()
        return self.stack2.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())