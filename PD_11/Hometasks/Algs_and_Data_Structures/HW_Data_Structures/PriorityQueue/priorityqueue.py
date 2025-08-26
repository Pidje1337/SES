

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, prev, next, priority):
            self.value = value
            self.prev = prev
            self.next = next
            self.priority = priority

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.head

    def dequeue(self):

        if self.is_empty():
            return None

        self.head = self.head.prev
        self.head.next = None

    def enqueue(self, node):
        buff = self.tail
        while buff.priority != node.priority:
            buff = buff.next
        node.next = buff
        node.prev = buff.prev
        buff.prev.next = node
        buff.prev = node


