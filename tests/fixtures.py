import pytest

from fourier.actors import Circle, LineAxes, MultiSineWave, SineWave


@pytest.fixture
def circle():
    """
    Instance of Circle.
    """
    return Circle(radius=2, x0=1, y0=-1)


@pytest.fixture
def sine_wave():
    """
    Instance of SineWave.
    """
    return SineWave(2)


@pytest.fixture
def line_axes():
    """
    Instance of LineAxes.
    """
    return LineAxes()


@pytest.fixture
def multi_sine_wave():
    s1 = SineWave.init_frequency(1)
    s2 = SineWave.init_frequency(2)
    ms = MultiSineWave()
    ms.append(s1)
    ms.append(s2)
    return ms
