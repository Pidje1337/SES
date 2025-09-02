from multiprocessing.managers import Value


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.size = 0
        self.head = None

    def add_first(self, value):

        node = self.Node(value)

        if not self.is_empty():
            node.next = self.head
        self.head = node

        self.size += 1

        return None

    def add_last(self, value):

        node = self.Node(value)

        if self.is_empty():
            self.head = node
        else:
            buff = self.head
            while buff.next is not None:
                buff = buff.next
            buff.next = node

        self.size += 1

        return None

    def insert(self, index, value):

        node = self.Node(value)

        if index-1 > self.size:
            raise ValueError
        if index == 0:
            self.add_first(value)
            return None
        if index == self.size:
            self.add_last(value)
            return None

        counter = 0
        buff = self.head.next
        while counter != index - 1:
            counter += 1
            buff = buff.next
        node.next = buff.next
        buff.next = node

        self.size += 1

    def remove(self, elem):

        if self.head.value == elem:
            self.head = self.head.next
            self.size -= 1
            return

        count = 0
        buff = self.head
        while count != self.size:
            if buff.next.value == elem:
                self.size -= 1
                buff.next = buff.next.next
                return
            buff = buff.next
            count += 1
        else:
            return -1

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

        return result.value

    def find(self, elem):

        if self.head.value == elem:
            return 0
        buff = self.head
        count = 1
        while buff.next is not None:
            if buff.value == elem:
                return count
            buff = buff.next
            count += 1

        return -1

    def on_index(self, index):

        if index > self.size - 1:
            raise ValueError

        counter = 0
        buff = self.head
        while counter != index:
            buff = buff.next
            counter += 1
        return buff.value
