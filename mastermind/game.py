import random

POOL = list(range(1, 7))
SIZE = 4

def play():
    ...


def new_secret():
    return random.sample(POOL, SIZE)

def validate_guess(guess, secret):
    if len(guess) < SIZE:
        return "Not enough values"
    if len(guess) > SIZE:
        return "Too many values"
    if len(set(guess)) < SIZE:
        seen = set()
        for val in guess:
            if val in seen:
                return f"Duplicate value '{val}' in guess"
            seen.add(val)
    for val in guess:
        if val not in POOL:
            return f"Invalid value '{val}' in guess"
