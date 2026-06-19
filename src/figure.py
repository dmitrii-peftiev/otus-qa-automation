from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    @property
    @abstractmethod
    def area(self) -> int | float:
        pass

    def add_area(self, figure: "Figure") -> int | float:
        if not isinstance(figure, Figure):
            raise ValueError(
                f"Argument figure must be Figure or child class, current {type(figure).__name__}"
            )
        return self.area + figure.area
