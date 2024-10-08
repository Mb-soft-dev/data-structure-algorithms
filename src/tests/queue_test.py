import pytest
from data_structures.queue import Queue

def test_init():
    queue = Queue()
    assert queue.isEmpty() == True
    assert queue.length() == 0
    assert queue.items() == []

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.length() == 3

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    assert queue.peek() == 2

def test_peek():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    assert queue.peek() == "A"