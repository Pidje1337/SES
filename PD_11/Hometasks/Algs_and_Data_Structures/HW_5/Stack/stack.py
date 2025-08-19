class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value, self.top)
        self.top = node
        self.size += 1