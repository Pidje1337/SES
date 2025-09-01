

class PriorityQueue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, priority):
            self.value = value
            self.prev = None
            self.next = None
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

        buff = self.head.value
        self.head = self.head.prev
        self.head.next = None

        self.size -= 1

        return buff

    def enqueue(self, value, priority):

        node = self.Node(value, priority)

        if self.is_empty():
            self.head = node
            self.tail = node
            self.size += 1
            return

        buff = self.tail
        if buff.priority == node.priority:
            buff.prev = node
            node.next = buff
            self.tail = node
            self.size += 1
            return

        while buff.priority < node.priority:
            buff = buff.next
        node.next = buff
        node.prev = buff.prev
        node.prev.next = node
        buff.prev = node

        self.size += 1

