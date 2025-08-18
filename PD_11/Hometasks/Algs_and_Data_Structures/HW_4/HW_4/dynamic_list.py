
from memory_emulation import malloc, realloc



class Custom_list:

    def __init__(self):

        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)


    def add(self, elem):

        if self.__count == self.__size:
            new_size = self.__size * self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)


        self.__memory[self.__count] = elem
        self.__count += 1


    def remove(self, elem):

        target_pos = -1

        for i in range(0, self.__count):
            if self.__memory[i] == elem:
                target_pos = i
                break

        if target_pos == -1:
            return

        for i in range(target_pos, self.__count -1, 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__count -= 1
        self.__memory[self.__count] = None


    def insert(self, index, elem):

        pass