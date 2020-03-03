attributes"""Module with AcademicBuilding class."""
from collections import Counter
import classroom


class AcademicBuilding:
    """Class for academic building representation."""

    def __init__(self, address: str, classrooms: list) -> None:
        """An instance of the class (academic building) with address,
        classrooms (a list of instances of the Classroom class) attributes
        initialization.

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        >>> building.classrooms
        [Classroom(016, 80, ['PC', 'projector', 'mic']), Classroom(007, 12, \
['TV']), Classroom(008, 25, ['PC', 'projector'])]
        """
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self) -> list:
        """Returns a list of tuples in (item, amount) format.

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('projector', 2), ('mic', 1), ('TV', 1)]
        """
        # Merges multiple lists into one
        qpmnt = []
        for clssrm in self.classrooms:
            qpmnt += clssrm.equipment

        # Counts the amount of each item in the merged list and returns the
        # results in the desired format
        ttl_qpmnt = dict(Counter(qpmnt))
        return [(item, ttl_qpmnt[item]) for item in ttl_qpmnt]

    def __str__(self):
        """Returns a user-friendly string representation of an instance of the
        class (academic building).

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        return self.address + '\n' + '\n'.join(clssrm.__str__()
                                               for clssrm in self.classrooms)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
