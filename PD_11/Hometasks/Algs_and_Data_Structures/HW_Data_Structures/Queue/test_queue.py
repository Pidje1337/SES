from queue import Queue
import pytest

example_queue = Queue()

def test_queue_initialization():
    assert example_queue.size == 0
    assert example_queue.tail is None
    assert example_queue.head is None
    assert example_queue.get_size() == 0
    assert example_queue.is_empty() is True
    assert example_queue.peek() is None

def test_queue_enqueue():
    example_queue.enqueue(4)
    assert example_queue.size == 1
    assert example_queue.head.value == 4
    assert example_queue.tail.value == 4
    example_queue.enqueue(2)
    assert example_queue.size == 2
    assert example_queue.head.value == 4
    assert example_queue.tail.value == 2
    assert example_queue.get_size() == 2

def test_queue_dequeue():
    example_queue.enqueue(4)
    example_queue.enqueue(2)
    assert example_queue.size == 2
    assert example_queue.tail.value == 2
    assert example_queue.head.value == 4
    assert example_queue.dequeue() == 4
    assert example_queue.size == 1
    assert example_queue.head.value == 2
    assert example_queue.tail.value == 2
    assert example_queue.dequeue() == 2
    assert example_queue.size == 0
    assert example_queue.is_empty() is True
    assert example_queue.dequeue() is None
    assert example_queue.size == 0
