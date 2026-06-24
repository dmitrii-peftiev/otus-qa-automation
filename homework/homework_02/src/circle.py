import math
from homework.homework_02.src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise ValueError(
                f"Circle radius must be above zero, current is radius={radius}"
            )

        self.radius = radius

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    @property
    def area(self) -> float:
        return math.pi * (self.radius**2)
