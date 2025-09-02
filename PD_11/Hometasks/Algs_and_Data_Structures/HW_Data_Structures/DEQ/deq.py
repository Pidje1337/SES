

class DEQ:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, next, prev):
            self.value = value
            self.next = next
            self.prev = prev

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.size = 0
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.value

    def peek_tail(self):
        return self.tail.value

    def enqueue(self, node):
        node.next = self.tail
        self.tail.prev = node
        self.tail = node

    def enqueue_head(self, node):
        node.prev = self.head
        self.head.next = node
        self.head = node

    def dequeue(self):
        self.head = self.head.prev
        self.head.next = None

    def dequeue_tail(self):
        self.tail = self.tail.next
        self.tail.prev = None

