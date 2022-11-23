import pytest
import os

# Задание 1
def zad1(bool):
    """
        Конвертирует заданное вами булевое значение в строку.
        >>> zad1(True)
        'True'
        >>> zad1(False)
        'False'
    """
    convert = str(bool)
    return convert

def test_zad1():
    assert zad1(True) == 'True'
    assert zad1(False) == 'False'

# Задание 2
def zad2(stroc):
    """
            Вводите строку и программа возвратит её в обратном порядке.
            >>> zad2("Helol, world!")
            '!dlrow ,loleH'
            >>> zad2("Batman")
            'namtaB'
    """
    stroc_rev = ''.join(reversed(stroc))
    return stroc_rev

def test_zad2():
    assert zad2("Helol, world!") == '!dlrow ,loleH'
    assert zad2("Batman") == 'namtaB'

# Задание 3
def zad3(arr):
    """
            Введите массив чисел и функция возвратит сумму всех положительных значений. Если массив пустой, то сумма равна 0.
            >>> zad3([2, -4, 5, 1, 0, -10])
            8
            >>> zad3([1, -4, 6, 4, 0, -10])
            11
    """
    mas_leng = len(arr)
    sum_m = 0
    i = 0
    while i < mas_leng:
        if arr[i] > 0:
            sum_m += arr[i]
        i += 1
    return  sum_m

def test_zad3():
    assert zad3([2, -4, 5, 1, 0, -10]) == 8
    assert zad3([1, -4, 6, 4, 0, -10]) == 11

# Задание 4
def zad4(a):
    """
                Введите высоту треугольника (целое положительное число ):
                >>> zad4(5)
                '     *\\n    ***\\n   *****\\n  *******\\n *********'
                >>> zad4(7)
                '       *\\n      ***\\n     *****\\n    *******\\n   *********\\n  ***********\\n *************'
    """
    arr = []
    for i in range(a, 0, -1):
        arr.append(i * ' ' + (a - i) * '*' + '*' + (a - i) * '*')
    return '\n'.join(arr)

def test_zad4():
    assert zad4(5) == '     *\n    ***\n   *****\n  *******\n *********'
    assert zad4(7) == '       *\n      ***\n     *****\n    *******\n   *********\n  ***********\n *************'

# Задание 5
def zad5(b):
    """
                Введите строку и программа подсчитает количество символов, которые встречаются более одного раза.
                >>> zad5("abbBBaahsyddh")
                4
                >>> zad5("dsfdsfsdcdfsFFs")
                3
    """
    sum_char = 0
    b = b.lower()
    for i in set(b):
        c = b.count(i)
        if c > 1:
            sum_char += 1
    return sum_char

def test_zad5():
    assert zad5("abbBBaahsyddh") == 4
    assert zad5("dsfdsfsdcdfsFFs") == 3

# Задание 6
def zad6(par):
    """
                Введите строку и программа преобразует её в стиль kebab-case (содержать символы в нижнем регистре).
                >>> zad6("camelsHaveThreeHumps")
                'camels-have-three-humps'
                >>> zad6("menGoodBye")
                'men-good-bye'
    """
    import re
    par = re.sub(r'(?<!^)(?=[A-Z])', '-', par)
    return par.lower()

def test_zad6():
    assert zad6("camelsHaveThreeHumps") == 'camels-have-three-humps'
    assert zad6("menGoodBye") == 'men-good-bye'

# Задание 7
def zad7(chis: int) -> int:
    """
                Введите целое число и программа преобразует его в другое:
                >>> zad7(565696)
                '253619'
                >>> zad7(38389696)
                '23282926'
    """
    if type(chis) != int:
        raise Exception('Input must be int')
    chis_long = str(chis)
    chis_mas = []
    otvet = ''

    for char in chis_long:
        if char in chis_mas:
            continue
        chis_count = chis_long.count(char)
        chis_mas.append(char)
        otvet += f'{chis_count}{char}'
    return otvet

def test_zad7():
    assert zad7(565696) == '253619'
    assert zad7(38389696) == '23282926'

# Задание 8
def zad8(mas_sev):
    """
                Введите массив чисел и отсортирует все нечетные числа в массиве по возрастанию, при этом четные числа останутся на своих местах:                >>> zad8([7, 8, 1, 5, 8, 6, 3])
                [1, 8, 3, 5, 8, 6, 7]
                >>> zad8([2, 10, 8, 25, 1, -10])
                [2, 10, 8, 1, 25, -10]
    """
    for i in range(len(mas_sev)):
        if mas_sev[i] % 2 != 0:
            for k in range(i, len(mas_sev)):
                if mas_sev[k] % 2 != 0 and mas_sev[i] > mas_sev[k]:
                    n = mas_sev[k]
                    mas_sev[k] = mas_sev[i]
                    mas_sev[i] = n
    return mas_sev

def test_zad8():
    assert zad8([7, 8, 1, 5, 8, 6, 3]) == [1, 8, 3, 5, 8, 6, 7]
    assert zad8([2, 10, 8, 25, 1, -10]) == [2, 10, 8, 1, 25, -10]

# Задание 9
def zad9(content, way_out) -> str:
    """
                Введите число и директорию задания (располагаються выше), что хотите преенести в текстовые файлы.
                В данном файле выведиться результат выполнения функций по выбраному заданию:
                >>> zad9(content=zad4(5), way_out='./lab_1/3.txt')

                >>> zad9(content=zad4(7), way_out='./lab_1/3.txt')

    """
    content = str(content)

    path = os.path.dirname(way_out)
    os.makedirs(path, exist_ok=True)

    with open(way_out, "a") as file:
        file.write(content + '\n')

def test_zad9(tmpdir):
    file = tmpdir.join('output.txt')
    zad9(content='Hello', way_out=file.strpath)
    assert file.read() == 'Hello\n'

    file = tmpdir.join('output2.txt')
    zad9(content='Test Alex', way_out=file.strpath)
    assert file.read() == 'Test Alex\n'


if __name__ == '__main__':
    print(zad1(True))
    print(zad2("Batman"))
    print(zad3([2, -4, 5, 1, 0, -10]))
    print(zad4(7))
    print(zad5("dsfdsfsdcdfsFFs"))
    print(zad6("camelsHaveThreeHumps"))
    print(zad7(565696))
    print(zad8([7, 8, 1, 5, 8, 6, 3]))
    print(zad9(content=zad4(5), way_out='./lab_1/3.txt'))
