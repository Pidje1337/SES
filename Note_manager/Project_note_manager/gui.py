from random import randint, uniform
from time import sleep

def launch_mock() -> None:
    rand_sum = 0
    while rand_sum <= 100:
        print("\rИдёт подготовка программы...", end="   [")
        print("\u25A0" * (rand_sum // 10), end="")
        print("." * (10 - rand_sum // 10), end="]")
        print(f"{rand_sum} %")
        rand_sum += randint(6, 14)
        sleep(uniform(0.4, 1.3))
    print(f"\r[" + "\u25A0" * 10 + f"]   {100}%\nПрограмма готова к работе!")
    return None