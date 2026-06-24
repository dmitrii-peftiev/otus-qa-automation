import pytest
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    "radius, perimeter",
    [pytest.param(3, 18.84, id="integer"), pytest.param(3.5, 21.99, id="float")],
)
def test_circle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == pytest.approx(perimeter, rel=1e-2), (
        f"Invalid perimeter for circle. Expected: {perimeter}, but received: {c.perimeter}"
    )


@pytest.mark.parametrize(
    "radius, area",
    [pytest.param(3, 28.27, id="integer"), pytest.param(3.5, 38.48, id="float")],
)
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.area == pytest.approx(area, rel=1e-2), (
        f"Invalid area for circle. Expected: {area}, but received: {c.area}"
    )


@pytest.mark.parametrize(
    "radius, side_a, side_b, side_c, add_area",
    [
        pytest.param(3, 3, 5, 7, 34.77, id="integer"),
        pytest.param(3.5, 3.5, 5.5, 7.5, 47.47, id="float"),
    ],
)
def test_circle_add_area(radius, side_a, side_b, side_c, add_area):
    c = Circle(radius)
    t = Triangle(side_a, side_b, side_c)
    total_area = c.add_area(t)
    assert total_area == pytest.approx(add_area, rel=1e-2), (
        f"Invalid add area for circle. Expected: {add_area}, but received: {total_area}"
    )


@pytest.mark.parametrize(
    "radius",
    [
        pytest.param(-3, id="negative_radius"),
        pytest.param(0, id="zero_radius"),
        pytest.param(False, id="boolean_radius"),
    ],
)
def test_circle_invalid_radius_values(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.skip(
    reason="PASSED, but TypeError needs to be handled. Report: https://t.me/c/chat_with_bugs"
)
@pytest.mark.parametrize(
    "radius",
    [
        pytest.param(None, id="none_radius"),
        pytest.param("abc", id="string_radius"),
        pytest.param("@#$", id="symbols_radius"),
    ],
)
def test_circle_invalid_radius_types(radius):
    with pytest.raises(TypeError):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, incorrect_obj",
    [
        pytest.param(3, -5, id="negative_add_area"),
        pytest.param(3, False, id="boolean_add_area"),
        pytest.param(3, None, id="none_add_area"),
        pytest.param(3, "abc", id="string_add_area"),
        pytest.param(3, "@#$", id="symbols_add_area"),
    ],
)
def test_circle_invalid_add_area(radius, incorrect_obj):
    c = Circle(radius)
    with pytest.raises(ValueError):
        c.add_area(incorrect_obj)
