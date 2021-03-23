"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 31.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17/12/2020
Дата последней модификации: 17/12/2020
Описание: Решение задачи № 31
#версия Python:3.9
"""
Нарисуйте полную блок-схему алгоритма сортировки массива «методом пузырька».
""
import random

n = 25
a = [random.randint(0, 100) for i in range(n)]
print(a)
N = 1
while N < n - 1:
    for i in range(n - N):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    N += 1
    
print(a)
