from sys import argv
import math

_, a, b, c = argv

a = int(a)
b = int(b)
c = int(c)

di = b ** 2 - 4 * a * c

if di == 0:
    x = -b / 2 * a
    print("Дискриминант равен 0", '\n', "x= ", x)
elif di > 0:
    x_1 = +b + math.sqrt(di) / 2 * a
    x_2 = -b + math.sqrt(di) / 2 * a
    print("Дискриминант больше 0", '\n', "x1= ", x_1, '\n', "x2= ", x_2)
else:
    print("Нет корней")


