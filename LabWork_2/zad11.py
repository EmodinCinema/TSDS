import pytest
import math
import cmath

def zad11(a, b, c, complex):
    """
        Введите числа три параметра a, b, c, если хотите высчитать в виде комплексных чисел то ещё и аргумент complex.
        Программа выведит результат решения квардратного уравнения.
        >>> zad11(2, 7, 1, True)
        'Комплексные корни уравнения: (-0.14921894064178787+0j) (-3.350781059358212+0j)'
        >>> zad11(2, 1, 2, False)
        'Нет решения'
    """

    if a == 0:
        return "Argument 'a' must be != 0"

    d = b ** 2 - 4 * a * c
    if complex:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        return f"Комплексные корни уравнения: {x1} {x2}"
    else:
        if d < 0:
            return "Нет решения"
        elif d == 0:
            x = -b / 2 * a
            return f"Корень уравнения: {x}"
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return f"Корни уравнения: {x1} {x2}"


def test_zad11():
    assert zad11(2, 7, 1, True) == 'Комплексные корни уравнения: (-0.14921894064178787+0j) (-3.350781059358212+0j)'
    zad11(2, 1, 2, False) == 'Нет решения'

if __name__ == "__main__":
    zad11(2, 7, 1, True)
