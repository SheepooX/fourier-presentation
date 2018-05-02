import pytest

from fourier.actors import Circle
from tests.fixtures import circle


def test_circle_properties(circle):
    assert 2 == circle.radius
    assert 1 == circle.x0
    assert -1 == circle.y0


def test_circle_properties_setters(circle):
    circle.radius = 0
    circle.x0 = 0
    circle.y0 = 3
    assert 0 == circle.radius
    assert 0 == circle.x0
    assert 3 == circle.y0


def test_circle_radius_error(circle):
    with pytest.raises(ValueError):
        circle.radius = -1


def test_circle_data_equal_length(circle):
    data = circle.data()
    assert len(data[0]) == len(data[1])
