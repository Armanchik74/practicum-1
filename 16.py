"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 16.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/12/2020
Дата последней модификации: 12/12/2020
Описание: Решение задачи № 16
#версия Python:3.9
"""
Известна денежная сумма. Разменять её купюрами 500, 100, 10 и монетой 2 руб., если это возможно.
""
Num = int(input("Денежная сумма:"))
if (Num % 2 == 1):
    print("Сумму нельзя разменять без остатка")
else:
    A = Num % 500
    A1 = Num // 500
    B = A % 100
    B1 = A // 100
    C = B % 10
    C1 = B // 10
    D = C % 2
    D1 = C // 2
    print(A1, "Купюр по 500")
    print(B1, "Купюр по 100")
    print(C1, "Купюр по 10")
    print(D1, "Купюр по 2")
