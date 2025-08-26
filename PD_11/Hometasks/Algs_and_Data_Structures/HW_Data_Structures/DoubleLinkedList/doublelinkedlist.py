

class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    class Node:

        def __init__(self, value, prev = None):
            self.value = value
            self.prev = prev
            self.next = None

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, value):

        if self.is_empty():
            self.head = value

        value.next = self.tail
        self.tail = value
        self.size += 1

    def add_last(self, value):

        if self.is_empty():
            self.tail = value
        else:
            value.prev = self.head

        self.head = value
        self.size += 1

    def insert(self, index, value):

        count = 0
        buff = self.tail
        while count != index:
            buff = buff.next
            count += 1
        value.prev = buff.prev
        value.next = buff
        buff.prev.next = value
        buff.prev = value

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def find(self, elem):

        index = 0
        buff = self.tail
        while index != self.size:
            if buff.value == elem:
                return index
            buff = buff.next
            index += 1

        return -1

    def remove(self, elem):

        buff = self.tail
        while buff.value != elem:
            buff = buff.next
        buff.next.prev = buff.prev
        buff.prev.next = buff.next
