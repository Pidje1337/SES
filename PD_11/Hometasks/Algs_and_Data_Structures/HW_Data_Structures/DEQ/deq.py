

class DEQ:

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    class Node:

        def __init__(self, value, next, prev):
            self.value = value
            self.next = next
            self.prev = prev

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def peek(self):
        return self.__head.value

    def peek_tail(self):
        return self.__tail.value

    def enqueue(self, node):
        node.next = self.__tail
        self.__tail.prev = node
        self.__tail = node

    def enqueue_head(self, node):
        node.prev = self.__head
        self.__head.next = node
        self.__head = node

    def dequeue(self):
        self.__head = self.__head.prev
        self.__head.next = None

    def dequeue_tail(self):
        self.__tail = self.__tail.next
        self.__tail.prev = None

