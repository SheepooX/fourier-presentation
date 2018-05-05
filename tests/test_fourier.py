import pytest
from fourier.fourier import average_point_location, get_shape
from tests.fixtures import sine_wave


def test_average_point_location():
    x = [0, 4, 0, 0]
    y = [1, 2, 3, 6]
    avg_loc = average_point_location(x, y)
    assert 1 == avg_loc[0]
    assert 3 == avg_loc[1]


def test_average_length_error():
    x = [1, 2, 3]
    y = [1, 2, 3, 4]
    with pytest.raises(ValueError):
        average_point_location(x, y)


def test_get_shape_error_winding_frequency(sine_wave):
    with pytest.raises(ValueError):
        get_shape(sine_wave, 0, 0, 1)
    with pytest.raises(ValueError):
        get_shape(sine_wave, 0, 0, 1)


def test_get_shape_error_a_b(sine_wave):
    with pytest.raises(ValueError):
        get_shape(sine_wave, 1, 5, 0)


def test_get_shape_equal_len(sine_wave):
    output = get_shape(sine_wave, 2, -1, 5)
    assert len(output.real) == len(output.imag)
