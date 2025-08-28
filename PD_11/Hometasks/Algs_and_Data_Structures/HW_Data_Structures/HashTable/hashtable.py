
class HashTable:

    collision_counter = 0

    def __init__(self):
        self.__count = 0
        self.__size = 1_000_000
        self.__reserved_keys = []
        self.__memory = [None] * self.__size

    def get_size(self) -> int:
        return self.__count

    def clear(self) -> None:
        HashTable.collision_counter = 0
        self.__count = 0
        self.__reserved_keys = []
        self.__memory = [None] * self.__size

    def is_empty(self) -> bool:
        return self.__count == 0

    def __hash(self, key: int) -> int:
        return hash(key) % self.__size

    def add(self, key: int, value: any) -> None:
        hash = self.__hash(key)

        if self.__memory[hash] is None:
            self.__memory[hash] = value
            if not isinstance(value, None):
                self.__count += 1
                self.__reserved_keys.append(key)
            return
        else:
            print(f"Collision for hash: {hash}")
            HashTable.collision_counter += 1

    def get_by_key(self, key: int) -> any:
        hash = self.__hash(key)
        value = self.__memory[hash]

        if value is None:  raise ValueError(f"Value not exists by key: {key}")

        return value

    def new_value_on_key(self, key: int, new_value: any) -> None:
        hash = self.__hash(key)

        if self.__memory[hash] is None:
            self.add(key, new_value)

        self.__memory[hash] = new_value

    def delete_by_key(self, key: int) -> None:
        self.new_value_on_key(key, None)

    def is_key_reserved(self, key: int) -> bool:
        hash = self.__hash(key)
        value = self.__memory[hash]
        return not (value is None)

    def print_keys(self):
        print(self.__reserved_keys)

    def print_values(self):
        for i in range(0, self.__count):
            hash = self.__hash(self.__reserved_keys[i])
            print(self.__memory[hash])

    def print_pairs(self):
        for i in range(self.__count):
            hash = self.__hash(self.__reserved_keys[i])
            print(self.__reserved_keys[i], ":", self.__memory[hash])