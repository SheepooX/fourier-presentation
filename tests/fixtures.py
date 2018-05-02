import pytest

from fourier.actors import Circle, LineAxes, SineWave


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
