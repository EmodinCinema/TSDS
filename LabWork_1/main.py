# Задание 1
def zad1(bool):
    convert = str(bool)
    return convert


# Задание 2
def zad2(stroc):
    stroc_rev = ''.join(reversed(stroc))
    return stroc_rev


# Задание 3
def zad3(arr):
    mas_leng = len(arr)
    sum_m = 0
    i = 0
    while i < mas_leng:
        if arr[i] > 0:
            sum_m += arr[i]
        i += 1
    return "Ответ", sum_m


# Задание 4
def zad4(a):
    arr = []
    for i in range(a, 0, -1):
        arr.append(i * ' ' + (a - i) * '*' + '*' + (a - i) * '*')
    return '\n'.join(arr)


# Задание 5
def zad5(b):
    sum_char = 0
    b = b.lower()
    for i in set(b):
        c = b.count(i)
        if c > 1:
            sum_char += 1
    return sum_char


# Задание 6
def zad6(par):
    import re
    par = re.sub(r'(?<!^)(?=[A-Z])', '-', par)
    return par.lower()


# Задание 7
def zad7(chis: int) -> int:
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


# Задание 8
def zad8(mas_sev):
    for i in range(len(mas_sev)):
        if mas_sev[i] % 2 != 0:
            for k in range(i, len(mas_sev)):
                if mas_sev[k] % 2 != 0 and mas_sev[i] > mas_sev[k]:
                    n = mas_sev[k]
                    mas_sev[k] = mas_sev[i]
                    mas_sev[i] = n
    return mas_sev


# Задание 9
def zad9(content, way_out) -> str:
    import os
    content = str(content)

    path = os.path.dirname(way_out)
    os.makedirs(path, exist_ok=True)

    with open(way_out, "a") as file:
        file.write(content + '\n')


if __name__ == '__main__':
    print(zad1(True))
    print(zad2("Helol, world!"))
    print(zad3([2, -4, 5, 1, 0, -10]))
    print(zad4(5))
    print(zad5("abbBBaahsyddh"))
    print(zad6("camelsHaveThreeHumps"))
    print(zad7(565696))
    print(zad8([7, 8, 1, 5, 8, 6, 3]))
    print(zad8([2, -4, 5, 1, 0, -10]))
    print(zad9(content=zad4(5), way_out='./lab_1/3.txt'))
