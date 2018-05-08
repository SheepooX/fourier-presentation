from fourier.actors import SineWave, MultiSineWave
from tests.fixtures import multi_sine_wave
import numpy as np
import pytest

def test_multi_sine_wave_fixture(multi_sine_wave):
    pass


def test_multi_sine_wave_equal_len(multi_sine_wave):
    data = multi_sine_wave.data(0, 5)
    assert len(data[0]) == len(data[1])


def test_multi_sine_wave_values(multi_sine_wave):
    data = multi_sine_wave.data(0, 5, 0.1)
    data1 = multi_sine_wave[0].data(0, 5, 0.1)
    data2 = multi_sine_wave[1].data(0, 5, 0.1)
    y = data1[1] + data2[1]
    assert np.array_equal(data1[0], data2[0])
    assert np.array_equal(data2[0], data[0])
    assert np.array_equal(y, data[1])


def test_multi_sine_wave_error_interval(multi_sine_wave):
    with pytest.raises(ValueError):
        multi_sine_wave.data(5, 0)


def test_multi_sine_wave_empty(multi_sine_wave):
    del multi_sine_wave[:]
    assert ([], []) == multi_sine_wave.data(0, 1)


def test_multi_sine_wave_indexing(multi_sine_wave):
    multi_sine_wave.append(123)
    assert 123 == multi_sine_wave[-1]
    assert 123 == multi_sine_wave[len(multi_sine_wave) -1]


def test_multi_sine_wave_slicing(multi_sine_wave):
    assert 1 == len(multi_sine_wave[1:])
