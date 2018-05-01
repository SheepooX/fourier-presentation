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
        if value < 0:
            raise ValueError(
                "Radius of a circle cannot be negative: {}".format(value))
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
    """
    Representation of an infinite sine wave.
    """

    @classmethod
    def init_period(klass, period, amplitude=1, x0=0, y0=0):
        """
        Initilize using period instead of angular velocity.

        Args:
            period: Period.
            (optional):
            amplitude: Amplitude.
            x0: X shift.
            y0: Y shift.
        
        Returns: Instance of SineWave.
        """
        return klass(2 * np.pi / period, amplitude, x0, y0)

    @classmethod
    def init_frequency(klass, frequency, amplitude=1, x0=0, y0=0):
        """
        Initilize using frequency instead of angular velocity.

        Args:
            frequency: Frequency.
            (optional):
            amplitude: Amplitude.
            x0: X shift.
            y0: Y shift.
        
        Returns: Instance of SineWave.
        """
        return klass.init_period(1 / frequency, amplitude, x0, y0)

    def __init__(self, angular_velocity, amplitude=1, x0=0, y0=0):
        """
        Args:
            angular_velocity: Angular velocity.
            amplitude: Amplitude.
            x0: X shift.
            y0: Y shift.
        """
        self.angular_velocity = angular_velocity
        self.amplitude = amplitude
        self.x0 = x0
        self.y0 = y0

    def __repr__(self):  # pragma: no cover
        return "SineWave(angular_frequency={}, amplitude={}, x0={}, y0={})".format(self.angular_velocity, self.amplitude, self.x0, self.y0)

    def data(self, x1, x2, step=default_step):
        """
        Calculate sine wave between two values x1 and x2.

        Args:
            x1: Left boundary.
            x2: Right boundary.
            (optional)
            step: Step of calculations.
        
        Raises:
            ValueError: The left boundary is greater than the right boundary.
        """
        if x1 > x2:
            raise ValueError("The left boundary is greater than the right boundary.")
        l = np.arange(x1, x2 + step, step)
        return l, self.amplitude * np.sin(self.angular_velocity * (l + self.x0) + self.y0)

    @property
    def angular_velocity(self):
        """
        Returns: Angular velocity.
        """
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, value):
        """
        Args:
            value: New angular velocity (>= 0)
        
        Raises:
            ValueError: Angular velocity has to be positive.
        """
        if value <= 0:
            raise ValueError(
                "Angular velocity has to be positive: {}".format(value))
        self._angular_velocity = value

    @property
    def period(self):
        """
        Returns: Period.
        """
        return 2 * np.pi / self.angular_velocity

    @period.setter
    def period(self, value):
        """
        Args:
            value: New period (>= 0).
        
        Raises:
            ValueError: Period has to be positive.
        """
        if value <= 0:
            raise ValueError("Period has to be positive: {}".format(value))
        self.angular_velocity = 2 * np.pi / value

    @property
    def frequency(self):
        """
        Returns: Frequency.
        """
        return 1 / self.period

    @frequency.setter
    def frequency(self, value):
        """
        Args:
            value: New frequency (>= 0).
        
        Raises:
            ValueError: Frequency has to be positive.
        """
        if value <= 0:
            raise ValueError("Frequency has to be positive: {}".format(value))
        self.period = 1 / value


class LineAxes:
    """
    Two lines that represent axes usually around origin.
    """

    def __init__(self, x_lim1=-1, x_lim2=1, y_lim1=-1, y_lim2=1):
        """
        Args:
            (optional)
            x_lim1: Left x boundary.
            x_lim2: Right x boundary.
            y_lim1: Bottom y boundary.
            y_lim2: Top y boundary.
        """
        if self._valid_interval(x_lim1, x_lim2) and self._valid_interval(y_lim1, y_lim2):
            self._x_lim1 = x_lim1
            self._x_lim2 = x_lim2
            self._y_lim1 = y_lim1
            self._y_lim2 = y_lim2
        else:
            raise ValueError("The arguments do not satisfy: x_lim1 < x_lim2 OR y_lim1 < y_lim2. x_lim1={}, x_lim2={}, y_lim1={}, y_lim2={}"
                             .format(x_lim1, x_lim2, y_lim1, y_lim2))

    def __repr__(self):  # pragma: no cover
        return "LineAxes(x_lim1={}, x_lim2={}, y_lim1={}, y_lim2={})".format(self.x_lim1, self.x_lim2, self.y_lim1, self.y_lim2)

    @staticmethod
    def _valid_interval(a, b):
        """
        Validates an interval.

        Args:
            a: Left value.
            b: Right value.

        Returns: True if a < b.
        """
        return a < b

    @property
    def x_lim1(self):
        """
        Returns: Left x boundary.
        """
        return self._x_lim1

    @x_lim1.setter
    def x_lim1(self, value):
        """
        Args:
            value: New left x boundary.

        Raises:
            ValueError: Left x_lim1 has to be smaller than right x_lim2.
        """
        if not self._valid_interval(value, self.x_lim2):
            raise ValueError(
                "Left x_lim1 has to be smaller than right x_lim2.")
        self._x_lim1 = value

    @property
    def x_lim2(self):
        """
        Returns: Right x boundary.
        """
        return self._x_lim2

    @x_lim2.setter
    def x_lim2(self, value):
        """
        Args:
            value: New right x boundary.

        Raises:
            ValueError: Left x_lim1 has to be smaller than right x_lim2.
        """
        if not self._valid_interval(self.x_lim1, value):
            raise ValueError(
                "Left x_lim1 has to be smaller than right x_lim2.")
        self._x_lim2 = value

    @property
    def y_lim1(self):
        """
        Returns: Bottom y boundary.
        """
        return self._y_lim1

    @y_lim1.setter
    def y_lim1(self, value):
        """
        Args:
            value: New bottom y boundary.

        Raises:
            ValueError: Bottom y_lim1 has to be smaller than top y_lim2.
        """
        if not self._valid_interval(value, self.y_lim2):
            raise ValueError(
                "Bottom y_lim1 has to be smaller than top y_lim2.")
        self._y_lim1 = value

    @property
    def y_lim2(self):
        """
        Returns: Top y boundary.
        """
        return self._y_lim2

    @y_lim2.setter
    def y_lim2(self, value):
        """
        Args:
            value: New top y boundary.

        Raises:
            ValueError: Bottom y_lim1 has to be smaller than top y_lim2.
        """
        if not self._valid_interval(self.y_lim1, value):
            raise ValueError(
                "Bottom y_lim1 has to be smaller than top y_lim2.")
        self._y_lim2 = value
