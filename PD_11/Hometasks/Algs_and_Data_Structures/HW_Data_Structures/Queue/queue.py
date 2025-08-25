

class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, prev):
            self.value = value
            self.prev = prev

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.head

    def enqueue(self, value: Node):

        if self.is_empty():

            self.head = value

        self.tail.prev = value
        self.tail = self.tail.prev

    def dequeue(self):
        buffer = self.head.value
        self.head = self.head.prev

        return buffer
