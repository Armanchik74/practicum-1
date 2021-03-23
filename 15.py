"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 15.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/12/2020
Дата последней модификации: 12/12/2020
Описание: Решение задачи № 15
#версия Python:3.9
"""
Дан номер места в плацкартном вагоне. Определить, какое это место: верхнее или нижнее, в купе или боковое.
""
Num = int(input("Укажите номер места в плацкартном вагоне:"))
if (Num > 60):
    print("Такого номера не существует, проверьте данные:")
elif (Num > 0 and Num < 35):
    print("Ваше место в купе")
else:
    print("Ваше место - боковое")
if (Num % 2 == 0):
    print("верхнее")
else:
    print("нижнее")