import pytest

from fourier.actors import Circle, SineWave


@pytest.fixture
def circle():
    return Circle(radius=2, x0=1, y0=-1)


@pytest.fixture
def sine_wave():
    return SineWave(2)