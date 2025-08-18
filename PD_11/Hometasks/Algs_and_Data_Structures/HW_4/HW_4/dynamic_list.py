
from memory_emulation import malloc, realloc



class Dynamic_list:

    def __init__(self, size: int):

        if not isinstance(size, int):
            raise TypeError("Incorrect input! Size of dynamic list must be a positive integer")
        if size < 0:
            raise ValueError("Incorrect input! Size of dynamic list must be greater or equal to zero")

        self.__count = 0
        self.__size = size
        self.__memory = malloc(self.__size)

    def check_and_realloc(self):

        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)



    # Element addition functions

    def add(self, elem):

        self.check_and_realloc()

        self.__memory[self.__count] = elem
        self.__count += 1


    def insert(self, index, elem):

        self.check_and_realloc()

        i = self.__count + 1
        while i != index:
            self.__memory[i] = self.__memory[i-1]
            i -= 1

        self.__memory[index] = elem


    def add_first(self, elem):

        self.insert(0, elem)



    # Element deletion functions

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


    def pop(self, index):

        for i in range(index, self.__count -1):
            self.__memory[i] = self.__memory[i+1]

        self.__count -= 1


    def clear(self):

        for i in range(self.__count):
            self.__memory[i] = None

        self.__count = 0



    # Element data functions

    def find(self, elem):

        target_pos = -1

        for i in range(self.__count):
            if self.__memory[i] == elem:
                target_pos = i
                break

        return target_pos

    def count(self, elem):

        result = 0

        for i in range(self.__count):
            if self.__memory[i] == elem:
                result += 1

        return result



    # Dynamic list properties functions

    def is_empty(self):

        if self.__count != 0:
            return False

        return True