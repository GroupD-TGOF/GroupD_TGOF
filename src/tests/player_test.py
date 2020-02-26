from frupal import Player


def test_player():
    p = Player(energy=1, money=1)
    assert p.position == (0,0)
