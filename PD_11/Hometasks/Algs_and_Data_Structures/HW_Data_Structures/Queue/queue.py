

class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0