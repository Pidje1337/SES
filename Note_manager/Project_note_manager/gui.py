from random import randint, uniform
from time import sleep

def launch_mock() -> None:
    rand_sum = 0
    while rand_sum < 100:
        output = "\rИдёт подготовка программы...   ["
        output += "\u25A0" * (rand_sum // 10)
        output += "." * (10 - rand_sum // 10) + "]"
        output += f"{rand_sum}%"
        print(output)
        rand_sum += randint(6, 14)
        sleep(uniform(0.4, 1.3))
    print(f"\r[" + "\u25A0" * 10 + f"]   {100}%\nПрограмма готова к работе!")
    return None