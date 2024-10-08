# Queue class
# A Queue is a data structure that follows the First In First out (FIFO) principle.
# This mean that the first element added to the queue will be the first one to be removed.
from data_structures.abstract_collection import AbstractCollection


class Queue(AbstractCollection): 

    ## Initialize the queue
    def __init__(self):
        self.queue = []
        self.size = 0

    ## Add an element to the queue
    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    ## Remove the first element in the queue
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.queue.pop(0)

    def peek(self):
        if self.size == 0:
            return None
        return self.queue[0]
    
    ## Check if the queue is empty
    def isEmpty(self):
        return self.size == 0

    ## Return all the elements
    def items(self):
        return self.queue

    ## Get the size
    def length(self):
        return self.size