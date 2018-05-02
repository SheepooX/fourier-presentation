import pytest

from fourier.actors import LineAxes
from tests.fixtures import line_axes


def test_line_axes_getters(line_axes):
    assert -1 == line_axes.x_lim1
    assert 1 == line_axes.x_lim2

    assert -1 == line_axes.y_lim1
    assert 1 == line_axes.y_lim2


def test_line_axes_setters(line_axes):
    line_axes.x_lim1 = -2
    assert -2 == line_axes.x_lim1
    line_axes.x_lim2 = 3
    assert 3 == line_axes.x_lim2
    line_axes.y_lim1 = 0
    assert 0 == line_axes.y_lim1
    line_axes.y_lim2 = 4
    assert 4 == line_axes.y_lim2


def test_line_axes_setters_error(line_axes):
    with pytest.raises(ValueError):
        line_axes.x_lim1 = 2
    with pytest.raises(ValueError):
        line_axes.x_lim2 = -2
    with pytest.raises(ValueError):
        line_axes.y_lim1 = 2
    with pytest.raises(ValueError):
        line_axes.y_lim2 = -2


def test_init_error():
    with pytest.raises(ValueError):
        LineAxes(x_lim1=1, x_lim2=-1)
    with pytest.raises(ValueError):
        LineAxes(y_lim1=1, y_lim2=-1)


def test_line_axes_interval():
    assert LineAxes._valid_interval(10, 15)
    assert not LineAxes._valid_interval(20, 15)
