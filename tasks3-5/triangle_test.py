"""Test module for triangle module."""
import point
from triangle import Triangle


print('#' * 13, "Subtask a", '#' * 14)
TRIANGLE = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
print("An instance of Triangle class TRIANGLE initialized.")

print('\n' + '#' * 13, "Subtask b", '#' * 14)
print("TRIANGLE.is_triangle():", TRIANGLE.is_triangle())

print('\n' + '#' * 13, "Subtask c", '#' * 14)
print("TRIANGLE.perimeter():", TRIANGLE.perimeter())

print('\n' + '#' * 13, "Subtask d", '#' * 14)
print("TRIANGLE.area():", TRIANGLE.area())
