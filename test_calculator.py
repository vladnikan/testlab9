import pytest
from calculator import Calculator


# 1. Тесты для add() — параметризация
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-5, 8, 3),
    (0, 0, 0),
    (100, -50, 50),
    (2.5, 3.7, 6.2),
])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected


# 2. Тесты для divide() — обычные + параметризация
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (7, 1, 7.0),
    (-15, 3, -5.0),
    (5, 2, 2.5),
])
def test_divide_normal(a, b, expected):
    assert Calculator.divide(a, b) == expected


# 3. Проверка исключения при делении на ноль
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль запрещено!"):
        Calculator.divide(10, 0)


# 4. Тесты для is_prime_number() — параметризация
@pytest.mark.parametrize("number, expected", [
    (2, True),   (3, True),   (5, True),   (7, True),
    (11, True),  (13, True),  (17, True),  (19, True),
    (1, False),  (0, False),  (-5, False), (4, False),
    (9, False),  (15, False), (25, False), (97, True),
    (100, False), (7919, True),  # 7919 — простое
])
def test_is_prime_number(number, expected):
    assert Calculator.is_prime_number(number) == expected