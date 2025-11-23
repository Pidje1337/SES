from bl_low import username_validation, does_user_exist
from datetime import date
from pathlib import Path


# Функция создания пользователя

def create_user():
    app_directory = Path(Path.home()/'note_manager_by_Kryutchkex')
    username = input("Введите имя пользователя, которого хотите создать: ")
    while not username_validation(username):
        username = input("Введённое имя пользователя содержит апрещённые символы или ошибки наименования"
                         "\nПожалуйста, введите другое имя пользователя, которого хотите создать: ")
    while does_user_exist(username):
        username = input("Данный пользователь уже существует!\nПожалуйста, введите другое имя пользователя, которого хотите создать: ")
    file = app_directory/f"{username}.txt"
    file.touch()
    file.write_text("Наименование, Тип заметки, Приоритет, Дата создания, Содержание")
