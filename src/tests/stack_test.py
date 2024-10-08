import pytest
from data_structures.stack import Stack

def test_init():
    stack = Stack()
    assert stack.isEmpty() == True
    assert stack.length() == 0
    assert stack.items() == []

def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.length() == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    assert stack.length() == 2

def test_peek():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    assert stack.peek() == "C"

def test_items():
    arr = [1,2,3]
    stack = Stack()
    stack.push(arr[0])
    stack.push(arr[1])
    stack.push(arr[2])
    assert stack.items() == arr