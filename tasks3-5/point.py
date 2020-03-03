"""Module with Point class."""


class Point:
    """Class for point representation."""

    def __init__(self, x: float, y: float) -> None:
        """An instance of the class (point) with x coordinate and y coordinate
        attributes initialization.

        >>> point2 = Point(3,1)
        >>> point2.x
        3
        >>> point2.y
        1
        >>> point3 = Point(2,3)
        >>> point3.x
        2
        >>> point3.y
        3
        """
        self.x = x
        self.y = y


if __name__ == '__main__':
    import doctest

    doctest.testmod()
