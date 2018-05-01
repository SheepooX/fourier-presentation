import pytest

from fourier.actors import Circle


@pytest.fixture
def circle():
    return Circle(radius=2, x0=1, y0=-1)
