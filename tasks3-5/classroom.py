"""Module with Classroom class."""


class Classroom:
    """Class for classroom representation."""

    def __init__(self, number: str, capacity: int, equipment: list) -> None:
        """An instance of the class (classroom) with number, capacity and
        equipment attributes initialization.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self) -> str:
        """Returns a user-friendly string representation of an instance of the
        class (classroom).

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        """
        return f"Classroom {self.number} has a capacity of {self.capacity} " \
               f"persons and has the following equipment: " \
               f"{', '.join(self.equipment)}."

    def is_larger(self, another_classroom) -> bool:
        """Returns True if classroom x is larger than classroom y and False
        otherwise.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return self.capacity > another_classroom.capacity

    def equipment_differences(self, another_classroom):
        """Returns a list of items that are in classroom x and not in classroom
        y.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        """
        return [item for item in self.equipment
                if item not in another_classroom.equipment]

    def __repr__(self):
        """Returns a developer-friendly string representation of an instance of
        the class (classroom).

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom(016, 80, ['PC', 'projector', 'mic'])
        """
        return f"Classroom({self.number}, {self.capacity}, {self.equipment})"


if __name__ == '__main__':
    import doctest

    doctest.testmod()
