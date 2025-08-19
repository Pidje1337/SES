

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    class Node:

        def __init__(self, value, next = None):
            self.value = value
            self.next = next

