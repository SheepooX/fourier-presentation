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
