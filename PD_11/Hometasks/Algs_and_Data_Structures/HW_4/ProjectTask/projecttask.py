from datetime import datetime


class ProjectTask:

    def __init__(self, description: str, duedate: datetime):

        self.description = description
        self.duedate = duedate

class TaskStack:

    class Node:

        def __init__(self, data):
            self.data = data
            self.prev = None

    def __init__(self):
        self.top = None
        self.size = 0

    def count(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.top.data

    def push(self, project):

        project = self.Node(project)

        project.prev = self.top
        self.top = project
        self.size += 1

    def pop(self):

        if self.size == 0:
            return None

        result = self.top.data
        self.top = self.top.prev
        self.size -= 1

        return result