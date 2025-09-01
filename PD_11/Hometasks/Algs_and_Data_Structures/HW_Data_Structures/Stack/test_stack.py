import pytest
from stack import Stack

stack_example = Stack()

def test_stack_initialization():
    assert stack_example.is_empty() is True
    assert stack_example.size == 0
    assert stack_example.peek() is None
    assert stack_example.pop() is None

def test_push_peek():
    stack_example.push("a")
    assert stack_example.size == 1
    assert stack_example.peek() == "a"
    stack_example.push("b")
    assert stack_example.size == 2
    assert stack_example.peek() == "b"

def test_peek_doesnt_pop():
    stack_example.push("a")
    stack_example.push("b")
    assert stack_example.peek() == "b"
    assert stack_example.size == 2
    assert stack_example.peek() == "b"
    assert stack_example.size == 2

def test_pop():
    for i in [2, 4, 6]:
        stack_example.push(i)
    assert stack_example.pop() == 6
    assert stack_example.size == 2
    assert stack_example.pop() == 4
    assert stack_example.size == 1
    assert stack_example.pop() == 2
    assert stack_example.size == 0
    assert stack_example.is_empty() is True
    assert stack_example.pop() is None
    assert stack_example.size == 0

def test_get_size():
    assert stack_example.get_size() == 0
    stack_example.push(4)
    assert stack_example.get_size() == 1