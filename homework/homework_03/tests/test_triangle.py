import pytest
from homework.homework_02.src.triangle import Triangle
from homework.homework_02.src.rectangle import Rectangle


@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter",
    [
        pytest.param(3, 5, 7, 15, id="integer"),
        pytest.param(3.5, 5.5, 7.5, 16.5, id="float"),
    ],
)
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, (
        f"Invalid perimeter for triangle. Expected: {perimeter}, but received: {t.perimeter}"
    )


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        pytest.param(3, 5, 7, 6.50, id="integer"),
        pytest.param(3.5, 5.5, 7.5, 8.99, id="float"),
    ],
)
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == pytest.approx(area, rel=1e-2), (
        f"Invalid area for triangle. Expected: {area}, but received: {t.area}"
    )


@pytest.mark.parametrize(
    "side_a1, side_b1, side_c, side_a2, side_b2, add_area",
    [
        pytest.param(3, 5, 7, 3, 5, 21.50, id="integer"),
        pytest.param(3.5, 5.5, 7.5, 3.5, 5.5, 28.24, id="float"),
    ],
)
def test_triangle_add_area(side_a1, side_b1, side_c, side_a2, side_b2, add_area):
    t = Triangle(side_a1, side_b1, side_c)
    r = Rectangle(side_a2, side_b2)
    total_area = t.add_area(r)
    assert total_area == pytest.approx(add_area, rel=1e-2), (
        f"Invalid add area for triangle. Expected: {add_area}, but received: {total_area}"
    )


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        pytest.param(-3, 5, 7, id="negative_side_a"),
        pytest.param(3, -5, 7, id="negative_side_b"),
        pytest.param(3, 5, -7, id="negative_side_c"),
        pytest.param(0, 5, 7, id="zero_side_a"),
        pytest.param(5, 0, 7, id="zero_side_b"),
        pytest.param(3, 5, 0, id="zero_side_c"),
        pytest.param(False, 5, 7, id="boolean_side_a"),
        pytest.param(3, False, 7, id="boolean_side_b"),
        pytest.param(3, 5, False, id="boolean_side_c"),
        pytest.param(1, 2, 10, id="invalid_sum_ab_less_c"),
        pytest.param(10, 2, 3, id="invalid_sum_bc_less_a"),
    ],
)
def test_triangle_invalid_sides_values(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.skip(
    reason="PASSED, but TypeError needs to be handled. Report: https://t.me/c/chat_with_bugs"
)
@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        pytest.param(None, 5, 7, id="none_side_a"),
        pytest.param(3, None, 7, id="none_side_b"),
        pytest.param(3, 5, None, id="none_side_c"),
        pytest.param("abc", 5, 7, id="string_side_a"),
        pytest.param(3, 5, "@#$", id="symbols_side_c"),
    ],
)
def test_triangle_invalid_sides_types(side_a, side_b, side_c):
    with pytest.raises(TypeError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b, side_c, t2",
    [
        pytest.param(3, 5, 7, -5, id="negative_add_area"),
        pytest.param(3, 5, 7, False, id="boolean_add_area"),
        pytest.param(3, 5, 7, None, id="none_add_area"),
        pytest.param(3, 5, 7, "abc", id="string_add_area"),
        pytest.param(3, 5, 7, "@#$", id="symbols_add_area"),
    ],
)
def test_triangle_invalid_add_area(side_a, side_b, side_c, t2):
    t1 = Triangle(side_a, side_b, side_c)
    with pytest.raises(ValueError):
        t1.add_area(t2)
