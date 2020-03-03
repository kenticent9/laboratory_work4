"""Test module for building module."""
import classroom
from building import AcademicBuilding

print('#' * 63, "Subtask a", '#' * 64)
CLASSROOM_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
CLASSROOM_007 = classroom.Classroom('007', 12, ['TV'])
CLASSROOM_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
CLASSROOMS = [CLASSROOM_016, CLASSROOM_007, CLASSROOM_008]
BUILDING = AcademicBuilding('Kozelnytska st. 2a', CLASSROOMS)
print("BUILDING.address:", BUILDING.address)
print("BUILDING.classrooms:", BUILDING.classrooms)

print('\n' + '#' * 63, "Subtask b", '#' * 64)
print("BUILDING.total_equipment():", BUILDING.total_equipment())

print('\n' + '#' * 63, "Subtask c", '#' * 64)
print("User-friendly string representation of the BUILDING:", BUILDING)
