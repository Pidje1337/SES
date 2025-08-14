
def check_type(value: any, req_type: any) -> None or ValueError:
    if not isinstance(value, req_type):
        raise ValueError(f"Ошибка: Некорректный тип входный данных.\nОжидалось: {req_type}\nПолучено: {type(value)}")