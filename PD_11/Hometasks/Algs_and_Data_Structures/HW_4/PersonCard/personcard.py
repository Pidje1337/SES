def check_type(var: any, req_type: any) -> None or TypeError:
    if not isinstance(var, req_type):
        raise TypeError(f"Incorrect input! excepted {req_type}, received {type(var)}")

class PersonCard:

    def __init__(self, name: str, age: int, occupation: str):

        check_type(name, str)
        check_type(age, int)
        check_type(occupation, str)

        self.name = name
        self.age = age
        self.occupation = occupation

class PersonList:

    class Node:

        def __init__(self, data: any):
            self.data = data
            self.next = None

    def __init__(self):
        self.count = 0
        self.head = None

    def total_people(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def clear_all(self):
        self.count = 0
        self.head = None

    def add_person(self, person):

        person = self.Node(person)

        person.next = self.head
        self.head = person

        self.count += 1

    def append_person(self, person):

        person = self.Node(person)

        if self.is_empty():
            self.add_person(person)
        else:
            buff = self.head
            while buff.next is not None:
                buff = buff.next
            buff.next = person

        self.count += 1

    def insert_person_at(self, index: int, person):

        if 0 < index or index > self.count:
            raise ValueError("Error: Incorrect index value")

        person = self.Node(person)

        if index == 0:
            self.add_person(person)
        elif index == self.count - 1:
            self.append_person(person)
        else:
            buff = self.head
            count = 0
            while count != index - 1:
                person = buff.next
                count += 1
            person.next = buff.next
            buff.next = person

        self.count += 1

    def remove_first_person(self):

        if self.count == 0:
            return None

        result = self.head.data
        self.head = self.head.next
        self.count -= 1

        return result

    def remove_last_person(self):

        if self.count == 0:
            return None

        buff = self.head
        while buff.next.next is not None:
            buff = buff.next
        result = buff.next.data
        buff.next = None

        self.count -= 1

        return result

    def remove_person_card(self, person):

        if self.count == 0:
            return None

        if person == self.head.data:
            self.head = self.head.next
            return None

        buff = self.head

        while buff.next.data != person or buff.next is not None:
            buff = buff.next
        if buff.next == person:
            buff.next = person.next
            self.count -= 1

        return None