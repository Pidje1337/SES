

class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, prev = None):
            self.value = value
            self.prev = prev
            self.next = None

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_last(self, value):

        if self.is_empty():
            self.tail = value
        else:
            value.prev = self.head

        self.head = value
        self.size += 1