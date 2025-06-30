

# Задание № 1

class Animal:

    def __init__(self, name: str, kind: str, age: int, sound: str = "roar"):
        self.name = name
        self.kind = kind
        self.age = age
        self.sound = sound

    def make_a_sound(self):
        return f"{self.kind}: {self.sound}!"

    def __str__(self):
        return f"Name: {self.name}\nKind: {self.kind}\nAge: {self.age}"



# Задание № 2

class Book:

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def open_a_page(self, page):
        if page > self.pages or page < 0:
            return f"Книга не открылась! Такой страницы в книге нет!"
        else:
            return f"Книга открылась! Вы на {page}-й странице!"

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.pages}"



# Задание № 3

class PassengerPlane:

    def __init__(self, manufactorer: str,
                 model: str,
                 num_of_passengers: int,
                 current_height: int,
                 current_velocity: float,
                 is_in_air: bool = False):
        self.manufactorer = manufactorer
        self.model = model
        self.num_of_passengers = num_of_passengers
        self.current_height = current_height
        self.current_velocity = current_velocity
        self.is_in_air = is_in_air

    def pullup(self):
        if self.is_in_air == False: # or self.current_velocity > 0:
            return "Самолёт уже на взлёте!"
        else:
            self.is_in_air = True
            return "Самолёт взлетает!"

    def land(self):
        if self.is_in_air:
            return "Самолёт уже посадили!"
        else:
            self.current_height = 0
            self.current_velocity = 0
            return "Самолёт посадили!"

    def change_height(self, value: int):
        if value < 0:
            return "Некорректное значение! Самолёт разобьётся!"
        elif value > 12000:
            return "Некорректное значение! Максимальная высота полёта - 12 000 м!"
        else:
            self.current_height = value

    def change_velocity(self, value: float, option: bool=True):
        if option:
            self.current_velocity += value
        elif not option and self.current_velocity < value:
            self.current_velocity = 0
        else:
            self.current_velocity -= value

    def __str__(self):
        return f"Производитель: {self.manufactorer}\nМодель: {self.model}\nВместимость: {self.num_of_passengers} чел.\nТекущая вцысота: {self.current_height}\nТекущая скорость: {self.current_velocity} м/с"



# Задание № 4

class MusicAlbum:

    def __init__(self, by: str, title: str, genre: str, playlist: list = []):
        self.by = by
        self.title = title
        self.genre = genre
        self.playlist = playlist

    def add_to_playlist(self, value):
        self.playlist.append(value)
        return "Трек добавлен!"

    def remove_from_playlist(self, value):
        if value not in self.playlist:
            return "Трек не найден!"
        else:
            self.playlist.remove(value)
            return "Трек удалён из списка!"

    def play_the_track(self, value):
        if value not in self.playlist:
            return "Трек не найден!"
        else:
            return f"Играет {self.by} - {value}"

    def __str__(self):
        return f"Исполнитель: {self.by}\nНазвание: {self.title}\nЖанр: {self.genre}\nКомпозиции: {self.playlist}"