from geometry import Geometry

def test_is_not_a_triangle():
    assert Geometry.is_triangle(6,6,6)

def test_is_a_triangle():
    assert Geometry.is_triangle(0, 1, 2)
