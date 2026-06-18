import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f"Triangle sides must be above zero, current is side_a={side_a} and side_b={side_b} and side_c={side_c}"
            )
        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError(
                f"Triangle sides must form a valid triangle, current is side_a={side_a} and side_b={side_b} and side_c={side_c}"
            )

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self) -> int | float:
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self) -> float:
        half_p = self.perimeter / 2
        return math.sqrt(
            half_p
            * (half_p - self.side_a)
            * (half_p - self.side_b)
            * (half_p - self.side_c)
        )
