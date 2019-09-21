import pytest


@pytest.mark.parametrize("a, b, expected", [
                            (2, 3, 5),
                            (3, 7, 10),
                            (-2, 5, 3),
                            (0.1, 0.2, 0.3)
])
def test_add(a, b, expected):
    from calculator import add
    result = add(a, b)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
                            (2, 3, -1),
                            (7, 3, 4),
                            (-2, 5, -7),
                            (0.1, 0.2, -0.1)
])
def test_subtract(a, b, expected):
    from calculator import subtract
    result = subtract(c,d)
    assert result == pytest.approx(expected)
