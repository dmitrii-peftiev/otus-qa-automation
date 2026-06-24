import pytest
from homework.homework_02.src.rectangle import Rectangle
from homework.homework_02.src.square import Square


@pytest.mark.parametrize(
    "side_a, side_b, perimeter",
    [pytest.param(3, 5, 16, id="integer"), pytest.param(3.5, 5.5, 18, id="float")],
)
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, (
        f"Invalid perimeter for rectangle. Expected: {perimeter}, but received: {r.perimeter}"
    )


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [pytest.param(3, 5, 15, id="integer"), pytest.param(3.5, 5.5, 19.25, id="float")],
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, (
        f"Invalid area for rectangle. Expected: {area}, but received: {r.area}"
    )


@pytest.mark.parametrize(
    "side_a1, side_b1, side_a2, add_area",
    [
        pytest.param(3, 5, 3, 24, id="integer"),
        pytest.param(3.5, 5.5, 3.5, 31.5, id="float"),
    ],
)
def test_rectangle_add_area(side_a1, side_b1, side_a2, add_area):
    r = Rectangle(side_a1, side_b1)
    s = Square(side_a2)
    total_area = r.add_area(s)
    assert total_area == add_area, (
        f"Invalid add area for rectangle. Expected: {add_area}, but received: {total_area}"
    )


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        pytest.param(-3, 5, id="negative_side_a"),
        pytest.param(3, -5, id="negative_side_b"),
        pytest.param(0, 5, id="zero_side_a"),
        pytest.param(3, 0, id="zero_side_b"),
        pytest.param(False, 5, id="boolean_side_a"),
        pytest.param(3, False, id="boolean_side_b"),
    ],
)
def test_rectangle_invalid_sides_values(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.skip(
    reason="PASSED, but TypeError needs to be handled. Report: https://t.me/c/chat_with_bugs"
)
@pytest.mark.parametrize(
    "side_a, side_b",
    [
        pytest.param(None, 5, id="none_side_a"),
        pytest.param(3, None, id="none_side_b"),
        pytest.param("abc", 5, id="string_side_a"),
        pytest.param(3, "@#$", id="symbols_side_b"),
    ],
)
def test_rectangle_invalid_sides_types(side_a, side_b):
    with pytest.raises(TypeError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b, r2",
    [
        pytest.param(3, 5, -5, id="negative_add_area"),
        pytest.param(3, 5, False, id="boolean_add_area"),
        pytest.param(3, 5, None, id="none_add_area"),
        pytest.param(3, 5, "abc", id="string_add_area"),
        pytest.param(3, 5, "@#$", id="symbols_add_area"),
    ],
)
def test_rectangle_invalid_add_area(side_a, side_b, r2):
    r1 = Rectangle(side_a, side_b)
    with pytest.raises(ValueError):
        r1.add_area(r2)
