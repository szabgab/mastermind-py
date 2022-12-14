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

