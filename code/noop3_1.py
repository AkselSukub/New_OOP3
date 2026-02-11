#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


class Triangle:
    def __init__(self, a=3, b=4, c=5):
        if not self._is_valid_triangle(a, b, c):
            print("Ошибка: такие стороны не могут образовать треугольник")
            a, b, c = 3, 4, 5
        self.a = a
        self.b = b
        self.c = c

    def _is_valid_triangle(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    def read(self):
        while True:
            try:
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))

                if self._is_valid_triangle(a, b, c):
                    self.a = a
                    self.b = b
                    self.c = c
                    break
                else:
                    print("Ошибка: такие стороны не могут образовать треугольник")
            except ValueError:
                print("Ошибка: введите числа")

    def display(self):
        print(
            f"Треугольник со сторонами: a={self.a:.2f}, b={self.b:.2f}, c={self.c:.2f}"
        )
        print(f"Периметр: {self.perimeter():.2f}")
        angles = self.calculate_angles()
        print(f"Углы: A={angles[0]:.1f}°, B={angles[1]:.1f}°, C={angles[2]:.1f}°")

    def set_sides(self, a=None, b=None, c=None):
        new_a = a if a is not None else self.a
        new_b = b if b is not None else self.b
        new_c = c if c is not None else self.c

        if self._is_valid_triangle(new_a, new_b, new_c):
            self.a = new_a
            self.b = new_b
            self.c = new_c
        else:
            print("Ошибка: такие стороны не могут образовать треугольник")

    def calculate_angles(self):
        try:
            # Угол A (противолежащий стороне a)
            cosA = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
            angleA = math.degrees(math.acos(cosA))

            # Угол B (противолежащий стороне b)
            cosB = (self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)
            angleB = math.degrees(math.acos(cosB))

            # Угол C (противолежащий стороне c)
            cosC = (self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)
            angleC = math.degrees(math.acos(cosC))

            return angleA, angleB, angleC
        except ValueError:
            return 60.0, 60.0, 60.0

    def perimeter(self):
        return self.a + self.b + self.c


class Equilateral(Triangle):
    def __init__(self, side=1):
        super().__init__(side, side, side)
        self._area = None

    def read(self):
        while True:
            try:
                side = float(input("Введите сторону равностороннего треугольника: "))
                if side > 0:
                    self.set_sides(side, side, side)
                    self._area = None
                    break
                else:
                    print("Ошибка: сторона должна быть положительной")
            except ValueError:
                print("Ошибка: введите число")

    def display(self):
        print(f"Равносторонний треугольник со стороной: {self.a:.2f}")
        print(f"Периметр: {self.perimeter():.2f}")
        print(f"Все углы: 60.0°")
        print(f"Площадь: {self.calculate_area():.2f}")

    def set_sides(self, a=None, b=None, c=None):
        if a is not None:
            if a > 0:
                self.a = a
                self.b = a
                self.c = a
                self._area = None
            else:
                print("Ошибка: сторона должна быть положительной")
        else:
            super().set_sides(a, b, c)
            if not self._is_equilateral():
                print("Внимание: треугольник больше не равносторонний")

    def _is_equilateral(self):
        return math.isclose(self.a, self.b) and math.isclose(self.b, self.c)

    def calculate_area(self):
        if self._area is None or not self._is_equilateral():
            self._area = (math.sqrt(3) / 4) * self.a**2
        return self._area

    def get_area(self):
        return self.calculate_area()


if __name__ == "__main__":
    print("1. Работа с обычным треугольником:")
    t1 = Triangle(3, 4, 5)
    t1.display()

    print("\n   Изменяем стороны на 5, 6, 7:")
    t1.set_sides(5, 6, 7)
    t1.display()

    print("\n2. Создание равностороннего треугольника:")
    eq1 = Equilateral(3)
    eq1.display()

    print("\n   Изменяем сторону на 5:")
    eq1.set_sides(5)
    eq1.display()

    print("\n3. Проверка наследования:")
    print(f"   Периметр равностороннего треугольника: {eq1.perimeter():.2f}")
    print(f"   Углы равностороннего треугольника: {eq1.calculate_angles()}")

    print("\n4. Ввод обычного треугольника с клавиатуры:")
    t2 = Triangle()
    t2.read()
    t2.display()

    print("\n5. Ввод равностороннего треугольника с клавиатуры:")
    eq2 = Equilateral()
    eq2.read()
    eq2.display()

    print("\n6. Демонстрация полиморфизма (список треугольников):")
    shapes = [Triangle(3, 4, 5), Equilateral(4), Triangle(5, 5, 8), Equilateral(6)]

    for i, shape in enumerate(shapes, 1):
        print(f"\n   Фигура {i}:")
        shape.display()
        if isinstance(shape, Equilateral):
            print(f"   Площадь (специальный метод): {shape.get_area():.2f}")

    print("\n7. Проверка обработки ошибок:")

    print("   Попытка создать недопустимый треугольник:")
    t3 = Triangle(1, 2, 10)

    print("\n   Попытка создать равносторонний треугольник с отрицательной стороной:")
    eq3 = Equilateral(-5)

    print("\n   Попытка изменить равносторонний треугольник на неравносторонний:")
    eq4 = Equilateral(5)
    print("   Исходный треугольник:")
    eq4.display()
    print("   Пытаемся изменить только одну сторону:")
    eq4.set_sides(a=10)
    eq4.display()
