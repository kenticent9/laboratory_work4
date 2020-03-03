"""Test module for classroom module."""
from classroom import Classroom

print('\n' + '#' * 71, "Subtask a", '#' * 71)
CLASSROOM_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
print("An instance of Classroom class CLASSROOM_016 initialized.")
print("CLASSROOM_016.number:", CLASSROOM_016.number)
print("CLASSROOM_016.capacity:", CLASSROOM_016.capacity)
print("CLASSROOM_016.equipment:", CLASSROOM_016.equipment)

print('\n' + '#' * 71, "Subtask b", '#' * 71)
print("User-friendly string representation of the CLASSROOM_016:",
      CLASSROOM_016)

print('\n' + '#' * 71, "Subtask c", '#' * 71)
CLASSROOM_007 = Classroom('007', 12, ['TV'])
print("An instance of Classroom class CLASSROOM_007 initialized.")
print("CLASSROOM_016.is_larger(CLASSROOM_007):",
      CLASSROOM_016.is_larger(CLASSROOM_007))

print('\n' + '#' * 71, "Subtask d", '#' * 71)
print("CLASSROOM_016.equipment_differences(CLASSROOM_007):",
      CLASSROOM_016.equipment_differences(CLASSROOM_007))
print("Developer-friendly string representation of the CLASSROOM_016:",
      CLASSROOM_016.__repr__())
print("Developer-friendly string representation of the CLASSROOM_016 in list:",
      [CLASSROOM_016.__repr__()])
