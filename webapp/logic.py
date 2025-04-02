from random import randint


def start():
    a = randint(0, 37)
    if a == 0:
        return print(f'a = {a} - green')
    if a % 2 == 0:
        return print(f'a = {a} - red')
    return print(f'a = {a} - black')

start()