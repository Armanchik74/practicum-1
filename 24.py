"""
Имя проекта: practicum-1
Номер версии: 1.0
Имя файла: Задание 24.py
Автор: 2020 © А.С. Манукян, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 12/12/2020
Дата последней модификации: 12/12/2020
Описание: Решение задачи № 24
#версия Python:3.9
"""
Даны вещественные положительные числа a, b, c, d. Выясните, может ли прямоугольник со сторонами a,b уместиться внутри прямоугольника со сторонами c,d так, чтобы каждая сторона внутреннего прямоугольника была параллельна или перпендикулярна стороне внешнего прямоугольника.
""
a = int(input("Введите сторуну а прямоугольника:"))
b = int(input("Введите сторуну b прямоугольника:"))
c = int(input("Введите сторуну c прямоугольника:"))
d = int(input("Введите сторуну d прямоугольника:"))

if a <= 0 or b <= 0 or c <= 0 or d <= 0:
    print("Сторона прямоугольника не может быть отрицательной, проверьте данные")

if ((a < c and b < d) or (a < d and b < c)):
    print("Прямоугольник ", a, b, "сможет уместиться внутри прямоугольника:(",c," ",d,")")
else:
    print("Прямоугольник ", a, b, "НЕ сможет уместиться внутри прямоугольника:(",c," ",d,")")