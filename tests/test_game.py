import mastermind.game as mm

def test_game():
    mm.play()
    assert True

def test_new_secret():
    secret = mm.new_secret()
    assert len(secret) == 4
    assert len(set(secret)) == 4
    assert set(secret).issubset(list(range(1, 7)))
