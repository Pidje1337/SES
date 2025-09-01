

class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, prev=None):
            self.value = value
            self.prev = prev

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.head.value

    def enqueue(self, value):

        if self.is_empty():
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.prev = self.Node(value)
            self.tail = self.tail.prev

        self.size += 1

    def dequeue(self):

        if self.is_empty():
            return None

        buffer = self.head.value
        self.head = self.head.prev
        self.size -= 1

        return buffer
