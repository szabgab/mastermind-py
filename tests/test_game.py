import random
import mastermind.game as mm

def test_game():
    mm.play()
    assert True

def test_new_secret():
    secret = mm.new_secret()
    assert len(secret) == mm.SIZE
    assert len(set(secret)) == mm.SIZE
    assert set(secret).issubset(mm.POOL)

def test_fixed_secret():
    random.seed(42)
    secret = mm.new_secret()
    # print(secret)
    assert secret == [6, 1, 5, 3]

def test_validate_guess():
    assert mm.validate_guess(guess=[1, 2, 3], secret=[1, 2, 3, 4]) == "Not enough values"
    assert mm.validate_guess(guess=[1, 2, 3, 4, 5], secret=[1, 2, 3, 4]) == "Too many values"
    assert mm.validate_guess(guess=[1, 2, 3, 3], secret=[1, 2, 3, 4]) == "Duplicate value '3' in guess"
    assert mm.validate_guess(guess=[1, 2, 3, 7], secret=[1, 2, 3, 4]) == "Invalid value '7' in guess"

    #assert mm.validate_guess(guess=[1, 2, 3, 4], secret=[1, 2, 3, 4]) == ['*', '*', '*', '*']
    #assert mm.validate_guess(guess=[1, 2, 5, 6], secret=[1, 2, 3, 4]) == ['*', '*']
    #assert mm.validate_guess(guess=[1, 5, 3, 6], secret=[1, 2, 3, 4]) == ['*', '*']
    #assert mm.validate_guess(guess=[1, 3, 4, 2], secret=[1, 2, 3, 4]) == ['*', '+', '+', '+']
    #assert mm.validate_guess(guess=[5, 4, 1, 6], secret=[1, 2, 3, 4]) == ['+', '+']
