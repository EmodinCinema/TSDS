from fastapi import FastAPI
from pydantic import BaseModel
import math
import cmath
from typing import Union, List
import uvicorn


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None


class Zad3_L(BaseModel):
    arr: List[Union[int, float]]


class Zad8_L(BaseModel):
    mas_sev: List[int]


class Zad11(BaseModel):
    a: Union[int, float]
    b: Union[int, float]
    c: Union[int, float]
    complex_flag: bool


app = FastAPI()


@app.post("/")
def root():
    return {"message": "Helol, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Задание 1
@app.get("/zad1/{boll_zn}")
def zad1(boll_zn: bool):
    convert = str(bool)
    return convert


# Задание 2
@app.get("/zad2/{stroc}")
def zad2(stroc: str):
    stroc_rev = ''.join(reversed(stroc))
    return stroc_rev


# Задание 3
@app.post("/zad3/")
def zad3(listting: Zad3_L) -> int:
    arr = listting.arr
    mas_lg = len(arr)
    sum_m = 0
    i = 0
    while i < mas_lg:
        if arr[i] > 0:
            sum_m += arr[i]
        i += 1
    return sum_m


# Задание 4
@app.get("/zad4/{a}")
def zad4(a: int):
    arr = []
    for i in range(a, 0, -1):
        arr.append(i * ' ' + (a - i) * '*' + '*' + (a - i) * '*')
    return '\n'.join(arr)


# Задание 5
@app.get("/zad5/{b}")
def zad5(b: str):
    sum_char = 0
    b = b.lower()
    for i in set(b):
        c = b.count(i)
        if c > 1:
            sum_char += 1
    return sum_char


# Задание 6
@app.post("/zad6/{par}")
def zad6(par: str):
    import re
    par = re.sub(r'(?<!^)(?=[A-Z])', '-', par)
    return par.lower()


# Задание 7
@app.post("/zad7/{chis}")
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
@app.post("/zad8/")
def zad8(let: Zad8_L):
    mas_sev = let.mas_sev
    for i in range(len(mas_sev)):
        if mas_sev[i] % 2 != 0:
            for k in range(i, len(mas_sev)):
                if mas_sev[k] % 2 != 0 and mas_sev[i] > mas_sev[k]:
                    n = mas_sev[k]
                    mas_sev[k] = mas_sev[i]
                    mas_sev[i] = n
    return mas_sev


# Задание 11
@app.post("/zad11/")
def solve(sp: Zad11):
    a = sp.a
    b = sp.b
    c = sp.c
    complex = sp.complex_flag

    d = b ** 2 - 4 * a * c
    if a != 0:
        if complex:
            x1 = (-b + cmath.sqrt(d)) / (2 * a)
            x2 = (-b - cmath.sqrt(d)) / (2 * a)
            return str(x1), str(x2)
        else:
            if d < 0:
                return None
            elif d == 0:
                x = -b / 2 * a
                return x
            else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                return x1, x2
    else:
        return None


if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, log_level="info", reload=True, debug=True)
