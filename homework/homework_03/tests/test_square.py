import pytest
from homework.homework_02.src.square import Square
from homework.homework_02.src.circle import Circle


@pytest.mark.parametrize(
    "side_a, perimeter",
    [pytest.param(3, 12, id="integer"), pytest.param(3.5, 14, id="float")],
)
def test_square_perimeter(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, (
        f"Invalid perimeter for square. Expected: {perimeter}, but received: {s.perimeter}"
    )


@pytest.mark.parametrize(
    "side_a, area",
    [pytest.param(3, 9, id="integer"), pytest.param(3.5, 12.25, id="float")],
)
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.area == area, (
        f"Invalid area for square. Expected: {area}, but received: {s.area}"
    )


@pytest.mark.parametrize(
    "side_a, radius, add_area",
    [
        pytest.param(3, 5, 87.54, id="integer"),
        pytest.param(3.5, 5.5, 107.28, id="float"),
    ],
)
def test_square_add_area(side_a, radius, add_area):
    s = Square(side_a)
    c = Circle(radius)
    total_area = s.add_area(c)
    assert total_area == pytest.approx(add_area, rel=1e-2), (
        f"Invalid add area for square. Expected: {add_area}, but received: {total_area}"
    )


@pytest.mark.parametrize(
    "side_a",
    [
        pytest.param(-3, id="negative_side"),
        pytest.param(0, id="zero_side"),
        pytest.param(False, id="boolean_side"),
    ],
)
def test_square_invalid_sides_values(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.skip(
    reason="PASSED, but TypeError needs to be handled. Report: https://t.me/c/chat_with_bugs"
)
@pytest.mark.parametrize(
    "side_a",
    [
        pytest.param(None, id="none_side"),
        pytest.param("abc", id="string_side"),
        pytest.param("@#$", id="symbols_side"),
    ],
)
def test_square_invalid_sides_types(side_a):
    with pytest.raises(TypeError):
        Square(side_a)


@pytest.mark.parametrize(
    "side_a, s2",
    [
        pytest.param(3, -5, id="negative_add_area"),
        pytest.param(3, False, id="boolean_add_area"),
        pytest.param(3, None, id="none_add_area"),
        pytest.param(3, "abc", id="string_add_area"),
        pytest.param(3, "@#$", id="symbols_add_area"),
    ],
)
def test_square_invalid_add_area(side_a, s2):
    s1 = Square(side_a)
    with pytest.raises(ValueError):
        s1.add_area(s2)
