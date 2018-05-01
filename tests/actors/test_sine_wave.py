import pytest
from numpy import pi

from fourier.actors import SineWave
from tests.actors.fixtures import sine_wave


def test_sine_wave_init_period():
    SineWave.init_period(1)


def test_sine_wave_init_frequency():
    SineWave.init_frequency(1)


def test_sine_wave_getters(sine_wave):
    assert 2 == sine_wave.angular_velocity
    assert pi == sine_wave.period
    assert 1 / pi == sine_wave.frequency


def test_sine_wave_setter_with_angular_velocity(sine_wave):
    sine_wave.angular_velocity = 1
    assert 1 == sine_wave.angular_velocity
    assert 2 * pi == sine_wave.period
    assert 1 / (2 * pi) == sine_wave.frequency


def test_sine_wave_setter_with_period(sine_wave):
    sine_wave.period = 2 * pi
    assert 1 == sine_wave.angular_velocity
    assert 2 * pi == sine_wave.period
    assert 1 / (2 * pi) == sine_wave.frequency


def test_sine_wave_setter_with_frequency(sine_wave):
    sine_wave.frequency = 1 / (2 * pi)
    assert 1 == sine_wave.angular_velocity
    assert 2 * pi == sine_wave.period
    assert 1 / (2 * pi) == sine_wave.frequency


setter_errors_test_cases = ("sine_wave", "value"), [(sine_wave(), 0), (sine_wave(), -1)]

@pytest.mark.parametrize(*setter_errors_test_cases)
def test_sine_wave_angular_velocity_error(sine_wave, value):
    with pytest.raises(ValueError):
        sine_wave.angular_velocity = value


@pytest.mark.parametrize(*setter_errors_test_cases)
def test_sine_wave_period_error(sine_wave, value):
    with pytest.raises(ValueError):
        sine_wave.period = value


@pytest.mark.parametrize(*setter_errors_test_cases)
def test_sine_wave_frequency_error(sine_wave, value):
    with pytest.raises(ValueError):
        sine_wave.frequency = value


def test_sine_wave_data_equal_length(sine_wave):
    data = sine_wave.data(x1=0, x2=5)
    assert len(data[0]) == len(data[1])
