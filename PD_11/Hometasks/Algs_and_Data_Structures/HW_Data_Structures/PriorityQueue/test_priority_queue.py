from priorityqueue import PriorityQueue
import pytest

example = PriorityQueue()

def test_pr_queue_initialization():
    assert example.size == 0
    assert example.get_size() == 0
    assert example.is_empty() is True
    assert example.head is None
    assert example.tail is None

def test_add_two_elem_w_eq_prior():
    example.enqueue(2, 1)
    assert example.size == 1
    assert example.get_size() == 1
    assert example.is_empty() is False
    assert example.head.value == 2
    assert example.tail.value == 2
    assert example.head.priority == 1
    assert example.tail.priority == 1
    example.enqueue(3, 1)
    assert example.size == 2
    assert example.get_size() == 2
    assert example.head.value == 2
    assert example.tail.value == 3
    assert example.head.priority == 1
    assert example.tail.priority == 1

def test_add_two_elem_w_ne_prior():
    example.enqueue(1, 2)
    assert example.head.value == 1
    assert example.tail.value == 1
    assert example.head.priority == example.tail.priority == 2
    example.enqueue(2, 1)
    assert example.head.value == 2
    assert example.head.priority == 1
    assert example.tail.value == 1
    assert example.tail.prirotiy == 2

def test_add_multiple_elem_w_ne_prior():
    example.enqueue(1, 3)
    example.enqueue(2, 2)
    example.enqueue(3, 1)
    assert example.size == 3
    assert example.is_empty() is False
    assert example.get_size() == 3
    assert example.head.value == 3
    assert example.head.priority == 1
    assert example.tail.value == 1
    assert example.tail.prirotiy == 3

def test_peek():
    example.enqueue(2, 1)
    assert example.peek() == 2

def test_dequeue():
    example.enqueue(2, 2)
    example.enqueue(3, 2)
    assert example.head.value == 2
    example.dequeue()
    assert example.head.value == 3
    assert example.size == 1