# Stack class
# A stack is a data structure that follows the Last In First out (LIFO) principle.
# This mean that the last element added to the stack in the first to be removed. 

from data_structures.abstract_collection import AbstractCollection


class Stack(AbstractCollection): 

    ## Initialize the stack
    def __init__(self):
        self.stack = []
        self.size = 0

    ## Add an element to the stack
    def push(self, value):
        self.stack.append(value)
        self.size += 1
    
    ## Remove the last element added to the stack
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.stack.pop()

    ## Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    ## Get the last element added to the stack 
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    ## Return all the elements in the stack
    def items(self):
        return self.stack

    ## Get the size of the stack
    def length(self):
        return self.size