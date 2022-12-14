import random

POOL = list(range(1, 7))
SIZE = 4

def play():
    ...


def new_secret():
    return random.sample(POOL, SIZE)
