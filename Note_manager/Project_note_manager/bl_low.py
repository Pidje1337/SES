import csv
from pathlib import Path
import os
import re
import shutil


# Проверка на то, что приложение установлено

def is_installed() -> bool:
    '''
    Функция проверяет наличие файлов приложения на жёстком диске
    :return True or False:
    '''
    return Path.exists(Path.home()/'note_manager_by_Kryutchkex')

# Функция установки программы

def install() -> None:
    '''
    Функция устанавливает программу
    '''
    Path.mkdir(Path.home()/'note_manager_by_Kryutchkex')
    return None
    

# Проверка списка пользователей на пустоту

def is_empty():
    app_directory = Path.home()/'note_manager_by_Kryutchkex'
    return len(list(app_directory.glob("*"))) == 0

# Проверка существования пользователя

def does_user_exist(username: str) -> bool:
    '''
    Функциям проверяет наличие пользователя в списке пользователей
    :param username:
    :return True or False:
    '''
    app_directory = Path.home()/'note_manager_by_Kryutchkex'
    users = list(app_directory.glob("*"))
    if username in users:
        return True
    return False

# Проверка имени пользователя на валидность

def username_validation(username):

    forbidden_chars = r'[<>:"/\\|?*\x00-\x1f]'
    forbidden_names = r'(?i)^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\..*)?$'
    forbidden_endings = r'[ .]$'

    if re.search(forbidden_chars, username):
        raise ValueError("Ошибка: Введённое имя пользователя содержит запрещённые символы")

    if re.search(forbidden_endings, username):
        raise ValueError("Ошибка: Имя пользователя не должно оканчиваться точкой или пробелом")

    if re.match(forbidden_names, username):
        raise ValueError("Ошибка: Имя пользователя содержит зарезервированные ОС слова")

    return True