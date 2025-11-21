import csv
from pathlib import Path
import os


# Проверка на то, что приложение установлено

def is_installed() -> bool:
    '''
    Функция проверяет наличие файлов приложения на жёстком диске
    :return True or False:
    '''
    return Path.is_dir()

# Проверка списка пользователей на пустоту

def is_empty():
    pass

# Проверка существования пользователя

def does_user_exist(username: str) -> bool:
    '''
    Функциям проверяет наличие пользователя в списке пользователей
    :param username:
    :return True or False:
    '''
    return username in users

# Проверка имени пользователя на валидность

def username_validation():