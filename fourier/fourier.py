import numpy as np

# from fourier.actors import Circle, LineAxes, SineWave


def average_point_location(x, y):
    """
    Calculates an average location of points.

    Args:
        x: X values.
        y: Y values.

    Returns: Tuple - X_avg, Y_avg.

    Raises:
        ValueError: The length of x-values != length of y-values.
    """
    if len(x) != len(y):
        raise ValueError("The length of x-values != length of y-values.")
    return sum(x) / len(x), sum(y) / len(y)


def get_shape(sine_wave, winding_frequency, a, b, step=0.1):
    """
    Winds a part of a sine wave around a circle with a winding frequency.

    Args:
        sine_wave: Instance of fourier.actors.SineWave
        winding_frequency: Winding frequency.
        a: Left boundary.
        b: Right boundary.
        (optional)
        step: Step of the calculation.
    
    Returns: Instance of numpy.ndarray with imaginary part.

    Raises:
        ValueError: Winding Frequency must be positive.
        ValueError: The following condition must be true: a < b.
    """
    if winding_frequency <= 0:
        raise ValueError("Winding Frequency must be positive.")
    if a >= b:
        raise ValueError("The following condition must be true: a < b.")
    x = np.arange(a, b + step, step)
    omega = 2 * np.pi * winding_frequency
    shape = sine_wave.data(a, b, step=step)[1] * (np.sin(omega * x) + 1j * np.cos(omega * x))
    return shape.real, shape.imag
