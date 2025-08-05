
def check_type(value, type):
    if not isinstance(value, type):
        raise TypeError(f"Неправильное входное значение")
