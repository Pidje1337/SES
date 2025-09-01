

class DoubleLinkedList:

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    class Node:

        def __init__(self, value, prev = None):
            self.value = value
            self.prev = prev
            self.next = None

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def add_first(self, value):

        if self.is_empty():
            self.__head = value

        value.next = self.__tail
        self.__tail = value
        self.__size += 1

    def add_last(self, value):

        if self.is_empty():
            self.__tail = value
        else:
            value.prev = self.__head

        self.__head = value
        self.__size += 1

    def insert(self, index, value):

        count = 0
        buff = self.__tail
        while count != index:
            buff = buff.next
            count += 1
        value.prev = buff.prev
        value.next = buff
        buff.prev.next = value
        buff.prev = value

    def clear(self):
        self.__tail = None
        self.__head = None
        self.__size = 0

    def find(self, elem):

        index = 0
        buff = self.__tail
        while index != self.__size:
            if buff.value == elem:
                return index
            buff = buff.next
            index += 1

        return -1

    def remove(self, elem):

        buff = self.__tail
        while buff.value != elem:
            buff = buff.next
        buff.next.prev = buff.prev
        buff.prev.next = buff.next

    def pop(self, index):

        if index is None:
            self.__head = self.__head.prev
            self.__head.next = None
        else:
            count = 0
            buff = self.__tail
            while count != index:
                buff = buff.next
            buff.prev = buff.next
            buff.next.prev = buff.prev