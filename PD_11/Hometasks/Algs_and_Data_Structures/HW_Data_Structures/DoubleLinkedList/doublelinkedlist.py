

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