attributes"""Module with Line and Triangle classes."""
import point


class Line:
    """Class for line representation."""

    def __init__(self, point1: point.Point, point2: point.Point) -> None:
        """An instance of class (line) with point1, point2 and, consequently,
        length attributes initialization.

        >>> a = Line(point.Point(1,1), point.Point(3,1))
        >>> a.length
        2.0
        >>> b = Line(point.Point(3,1), point.Point(2,3))
        >>> b.length
        2.23606797749979
        """
        # Calculates the length of the line
        self.length = ((point2.x - point1.x)**2 +
                       (point2.y - point1.y)**2)**(1 / 2)


class Triangle:
    """Class for triangle representation."""

    def __init__(self, point1: point.Point, point2: point.Point,
                 point3: point.Point) -> None:
        """An instance of class (triangle) with point1, point2 and point3
        attributes initialization.

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.a
        2.0
        >>> triangle.b
        2.23606797749979
        """
        self.a = Line(point1, point2).length
        self.b = Line(point2, point3).length
        self.c = Line(point3, point1).length

    def is_triangle(self) -> bool:
        """Returns True if the triangle exists and False otherwise.

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        # Reassigns self variables for shorter code below
        a = self.a
        b = self.b
        c = self.c
        return False if a < 0 or b < 0 or c < 0 or \
                        (a + b) < c or (a + c) < b or (b + c) < a else True

    def perimeter(self) -> float:
        """Returns the perimeter of the triangle.

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        return self.a + self.b + self.c

    def area(self) -> float:
        """Returns the area of the triangle calculated via Heron's formula.

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**(1 / 2)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
