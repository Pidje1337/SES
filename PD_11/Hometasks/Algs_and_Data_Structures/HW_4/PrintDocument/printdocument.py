

class PrintDocument:

    def __init__(self, title: str, num_of_pages: int):
        self.title = title
        self.num_of_pages = num_of_pages

class PrintQueue:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def count(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.head

    def enqueue(self, document):

        document = self.Node(document)

        if self.is_empty():
            self.head = document

        document.next = self.tail
        self.tail = document

        self.size += 1

    def dequeue(self):

        if self.is_empty():
            return None

        result = self.head.data
        self.head = self.head.prev

        self.size -= 1

        return result
