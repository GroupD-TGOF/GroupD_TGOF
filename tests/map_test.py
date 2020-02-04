import pytest
from frupal import Map, Tile


def test_map_1():
    m = Map(5, 4)
    print(m)
    print(len(m._array[0]))
    m[2][1] = Tile('B', 1, False)
    print(m)
    print(m.get_size)

def test_map_construction():
    m = Map(5, 4)
    m = Map(1, 1)
    m = Map(100, 1)

def test_map_access():
    m = Map(5, 4)
    new_value = 'TEST'
    m[2][1] = Tile(new_value, 1, False)
    print(m)
    expected_map = """\
****** FOR DEBUG PURPOSE ONLY
tile, tile, tile, tile, tile, 
tile, tile, TEST, tile, tile, 
tile, tile, tile, tile, tile, 
tile, tile, tile, tile, tile, 
"""
    assert str(m) == expected_map
    # Test another assignment
    m[3][2] = Tile(new_value, 1, False)
    expected_map2 = """\
****** FOR DEBUG PURPOSE ONLY
tile, tile, tile, tile, tile, 
tile, tile, TEST, tile, tile, 
tile, tile, tile, TEST, tile, 
tile, tile, tile, tile, tile, 
"""
    assert str(m) == expected_map2


def test_map_get_size():
    expected = (5, 4)
    m = Map(*expected) # same as Map(5, 4)
    print(m.get_size)
    assert m.get_size == expected

@pytest.mark.skip('Skipping until config is implemented')
def test_map_generation():
    # TODO(nick) implement test once config is finished
    Map.generate_map(None)
    assert False


