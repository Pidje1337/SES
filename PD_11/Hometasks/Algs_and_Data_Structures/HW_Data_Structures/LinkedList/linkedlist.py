

class LinkedList:

    def __init__(self):
        self.__size = 0
        self.__head = None

    class Node:

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__size = 0
        self.__head = None

    def add_first(self, node):

        if not self.is_empty():
            node.next = self.__head
        self.__head = node

        self.__size += 1

    def add_last(self, node):

        if self.is_empty():
            self.__head = node
        else:
            buff = self.__head
            while buff.next is not None:
                buff = buff.next
            buff.next = node

        self.__size += 1

    def insert(self, index, node):

        buff = self.__head
        count = 0
        if index == 0:
            self.add_first(node)
        else:
            while count != index - 1:
                buff = buff.next
            node.next = buff.next
            buff.next = node

        self.__size += 1

    def remove(self, elem):

        if self.__head == elem:
            self.__head = self.__head.next
        else:
            count = 0
            buff = self.__head
            while buff.next.value != elem and count != self.__size:
                buff = buff.next
                count += 1
            if buff.next is not None:
                buff.next = buff.next.next

        self.__size -= 1

    def pop(self, index):

        if index is None:
            buff = self.__head
            while buff.next.next is not None:
                buff = buff.next
            result = buff.next
            buff.next = None
        else:
            result = 0
            buff = self.__head
            while result != index - 1:
                buff = buff.next
                result += 1
            result = buff.next
            buff.next = buff.next.next

        self.__size -= 1

        return result

    def find(self, elem):

        if self.__head.value == elem:
            return 0
        buff = self.__head
        count = 0
        while buff.next is not None:
            if buff.value == elem:
                return count
            buff = buff.next
            count += 1

        return -1


