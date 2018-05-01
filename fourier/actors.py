import numpy as np

default_step = 0.1


class Circle:
    """
    Representation of a circle that calculates its points for plotting.
    """

    def __init__(self, radius, x0, y0):
        """
        Args:
            radius: Radius of the circle.
            x0: X coordinate of the center.
            y0: Y coordinate of the center.
        """
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
    
    def __repr__(self):  # pragma: no cover
        return "Circle(radius={}, x0={}, y0={})".format(self.radius, self.x0, self.y0)
    
    @property
    def data(self, step=default_step):
        """
        Returns x, y arrays of circle points.

        Args:
            step (optional: Angle step of the calculation.
        
        Returns: Tuple of two numpy arrays.
        """
        l = np.arange(0, 2 * np.pi + step, step)
        return np.cos(l), np.sin(l)
    
    @property
    def radius(self):
        """
        Returns: Radius.
        """
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """
        Sets the radius (not negative) of the circle.

        Args:
            value: The new radius.
        """
        if value < 0: raise ValueError("Radius of a circle cannot be negative: {}".format(value))
        self._radius = value
    
    @property
    def x0(self):
        """
        Returns: x0
        """
        return self._x0
    
    @x0.setter
    def x0(self, value):
        """
        Args:
            value: The new x0.
        """
        self._x0 = value

    @property
    def y0(self):
        """
        Returns: y0
        """
        return self._y0
    
    @y0.setter
    def y0(self, value):
        """
        Args:
            value: The new y0.
        """
        self._y0 = value


class SineWave:

    @classmethod
    def init_period(klass, period, amplitude=1, x0=0, y0=0):
        return klass(2 * np.pi / period, amplitude, x0, y0)
    
    @classmethod
    def init_frequency(klass, frequency, amplitude=1, x0=0, y0=0):
        return klass(2 * np.pi * frequency, amplitude, x0, y0)

    def __init__(self, angular_velocity, amplitude=1, x0=0, y0=0):
        self.angular_velocity = angular_velocity
        self.amplitude = amplitude
        self.x0 = x0
        self.y0 = y0
    
    def __repr__(self):  # pragma: no cover
        return "SineWave(angular_frequency={}, amplitude={}, x0={}, y0={})".format(self.angular_velocity, self.amplitude, self.x0, self.y0)

    @property
    def angular_velocity(self):
        return self._angular_velocity
    
    @angular_velocity.setter
    def angular_velocity(self, value):
        if value <= 0:
            raise ValueError("Angular velocity has to be positive: {}".format(value))
        self._angular_velocity = value
    
    @property
    def period(self):
        return 2 * np.pi / self.angular_velocity
    
    @period.setter
    def period(self, value):
        if value <= 0:
            raise ValueError("Period has to be positive: {}".format(value))
        self.angular_velocity = 2 * np.pi / value
    
    @property
    def frequency(self):
        return 1 / self.period
    
    @frequency.setter
    def frequency(self, value):
        if value <= 0:
            raise ValueError("Frequency has to be positive: {}".format(value))
        self.period = 1 / value
