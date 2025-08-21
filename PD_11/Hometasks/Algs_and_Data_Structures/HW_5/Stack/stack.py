
class Stack:

    class Node:

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = self.Node(value, self.top)
        self.top = node
        self.size += 1

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def pop(self):

        if self.is_empty():
            return None

        buff = self.top
        self.top = self.top.next
        self.size -= 1

        return buff