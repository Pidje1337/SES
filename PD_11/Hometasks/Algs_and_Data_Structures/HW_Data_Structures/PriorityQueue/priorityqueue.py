

class PriorityQueue:

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    class Node:

        def __init__(self, value, prev, next, priority):
            self.value = value
            self.prev = prev
            self.next = next
            self.priority = priority

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def peek(self):
        return self.__head

    def dequeue(self):

        if self.is_empty():
            return None

        self.__head = self.__head.prev
        self.__head.next = None

    def enqueue(self, node):
        buff = self.__tail
        while buff.priority != node.priority:
            buff = buff.next
        node.next = buff
        node.prev = buff.prev
        buff.prev.next = node
        buff.prev = node


