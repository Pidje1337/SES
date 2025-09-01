
class Stack:

    class Node:

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, value):
        node = self.Node(value, self.__top)
        self.__top = node
        self.__size += 1

    def peek(self):

        if self.is_empty():
            return None

        return self.__top.value

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def pop(self):

        if self.is_empty():
            return None

        buff = self.__top
        self.__top = self.__top.next
        self.__size -= 1

        return buff