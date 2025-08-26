

class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    class Node:

        def __init__(self, value, next):
            self.value = value
            self.next = next

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.size = 0
        self.head = None

    def add_first(self, node):

        if not self.is_empty():
            node.next = self.head
        self.head = node

        self.size += 1

    def add_last(self, node):

        if self.is_empty():
            self.head = node
        else:
            buff = self.head
            while buff.next is not None:
                buff = buff.next
            buff.next = node

        self.size += 1

    def insert(self, index, node):

        buff = self.head
        count = 0
        if index == 0:
            self.add_first(node)
        else:
            while count != index - 1:
                buff = buff.next
            node.next = buff.next
            buff.next = node

        self.size += 1

    def remove(self, elem):

        if self.head == elem:
            self.head = self.head.next
        else:
            count = 0
            buff = self.head
            while buff.next.value != elem and count != self.size:
                buff = buff.next
                count += 1
            if buff.next is not None:
                buff.next = buff.next.next

        self.size -= 1

    def pop(self, index):

        if index is None:
            buff = self.head
            while buff.next.next is not None:
                buff = buff.next
            result = buff.next
            buff.next = None
        else:
            result = 0
            buff = self.head
            while result != index - 1:
                buff = buff.next
                result += 1
            result = buff.next
            buff.next = buff.next.next

        self.size -= 1

        return result

    def find(self, elem):

        if self.head.value == elem:
            return 0
        buff = self.head
        count = 0
        while buff.next is not None:
            if buff.value == elem:
                return count
            buff = buff.next
            count += 1

        return -1


