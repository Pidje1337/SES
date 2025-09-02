
from linkedlist import LinkedList
import pytest

example = LinkedList()

def test_linked_list_initialization():
    assert example.size == 0
    assert example.head is None
    assert example.is_empty() is True
    assert example.get_size() == 0

def test_add_and_remove():

    example.add_first(0)
    assert example.size == 1
    assert example.head.value == 0
    assert example.head.next is None
    assert example.get_size() == 1
    example.add_first(2)
    assert example.size == 2
    assert example.head.value == 2
    assert example.head.next.value == 0
    assert example.get_size() == 2
    example.insert(0, 4)
    assert example.get_size() == 3
    assert example.head.value == 4
    assert example.on_index(0) == 4
    assert example.on_index(1) == 2
    assert example.on_index(2) == 0
    example.add_last(6)
    assert example.on_index(3) == 6
    assert example.get_size() ==4
    example.insert(4, 10)
    assert example.get_size() == 5
    assert example.on_index(4) == 10

    example.insert(2, 3)
    example.insert(3, 4)

    assert example.on_index(2) == 3
    assert example.on_index(3) == 4

    example.remove(2)

    assert example.get_size() == 6
    assert example.remove(14) == -1
    example.remove(4)
    assert example.get_size() == 5



