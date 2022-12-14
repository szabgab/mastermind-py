import random


def play():
    ...


def new_secret():
    pool = list(range(1, 7))
    return random.sample(pool, 4)
