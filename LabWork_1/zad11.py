import math
import cmath
import argparse

parser = argparse.ArgumentParser(description='task_11 (solve: ax^2 + bx + c)')

parser.add_argument('a', type=int, help='Input a (for ax^2 + bx + c)')
parser.add_argument('b', type=int, help='Input b (for ax^2 + bx + c)')
parser.add_argument('c', type=int, help='Input c (for ax^2 + bx + c)')
parser.add_argument('-C', '--complex_flag', action="store_true", default=False, help='convert to complex_flag')


def solve(a, b, c, complex):
    d = b ** 2 - 4 * a * c
    if complex:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        print("Комплексные корни уравнения: ", x1, x2)
    else:
        if d < 0:
            print("Нет решения")
        elif d == 0:
            x = -b / 2 * a
            print("Корень уравнения:", x)
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("Корни уравнения: ", x1, x2)

def main():
    arguments = parser.parse_args()
    a = arguments.a
    b = arguments.b
    c = arguments.c
    complex = arguments.complex_flag
    if a == 0:
        print("Argument 'a' must be != 0")
    else:
        solve(a, b, c, complex)


if __name__ == "__main__":
    main()
