

class Queue:

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    class Node:

        def __init__(self, value, prev):
            self.value = value
            self.prev = prev

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def peek(self):
        return self.__head

    def enqueue(self, value: Node):

        if self.is_empty():

            self.__head = value

        self.__tail.prev = value
        self.__tail = self.__tail.prev

    def dequeue(self):

        if self.is_empty():
            return None

        buffer = self.__head.value
        self.__head = self.__head.prev

        return buffer
