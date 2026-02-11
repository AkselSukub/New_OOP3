#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
import math


class Reader:
    """Вспомогательный класс для ввода данных с клавиатуры"""

    @staticmethod
    def read_float(prompt):
        """Чтение вещественного числа"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число")

    @staticmethod
    def read_int(prompt):
        """Чтение целого числа"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите целое число")


class Root(ABC):
    """Абстрактный базовый класс для корней уравнений"""

    @abstractmethod
    def calculate_roots(self):
        """Абстрактный метод вычисления корней"""
        pass

    @abstractmethod
    def display(self):
        """Абстрактный метод вывода результата"""
        pass

    @abstractmethod
    def __str__(self):
        """Строковое представление уравнения"""
        pass

    def __repr__(self):
        """Представление для отладки"""
        return str(self)


class Linear(Root):
    """Класс для линейного уравнения: a*x + b = 0"""

    def __init__(self, a=1, b=0):
        if a == 0:
            raise ValueError(
                "Коэффициент a не может быть равен 0 для линейного уравнения"
            )
        self.a = a
        self.b = b
        self.roots = []
        self.calculate_roots()  # вычисляем корни сразу при создании

    @classmethod
    def read_from_keyboard(cls):
        """Создание объекта через ввод с клавиатуры"""
        print("Введите коэффициенты линейного уравнения a*x + b = 0")
        a = Reader.read_float("a = ")
        b = Reader.read_float("b = ")

        while a == 0:
            print("Коэффициент a не может быть равен 0 для линейного уравнения")
            a = Reader.read_float("a = ")

        return cls(a, b)

    def calculate_roots(self):
        """Вычисление корня линейного уравнения: x = -b/a"""
        try:
            root = -self.b / self.a
            self.roots = [root]
            return self.roots
        except ZeroDivisionError:
            self.roots = []
            return self.roots

    def display(self):
        """Вывод уравнения и его корней"""
        print(f"Уравнение: {self}")
        if self.roots:
            print(f"Корень: x = {self.roots[0]:.2f}")
        else:
            print("Корней нет")

    def __str__(self):
        """Строковое представление линейного уравнения"""
        b_sign = "+" if self.b >= 0 else "-"
        b_abs = abs(self.b)
        return f"{self.a:.2f}*x {b_sign} {b_abs:.2f} = 0"


class Square(Root):
    """Класс для квадратного уравнения: a*x^2 + b*x + c = 0"""

    def __init__(self, a=1, b=0, c=0):
        if a == 0:
            raise ValueError(
                "Коэффициент a не может быть равен 0 для квадратного уравнения"
            )
        self.a = a
        self.b = b
        self.c = c
        self.roots = []
        self.calculate_roots()  # вычисляем корни сразу при создании

    @classmethod
    def read_from_keyboard(cls):
        """Создание объекта через ввод с клавиатуры"""
        print("Введите коэффициенты квадратного уравнения a*x^2 + b*x + c = 0")
        a = Reader.read_float("a = ")
        b = Reader.read_float("b = ")
        c = Reader.read_float("c = ")

        while a == 0:
            print("Коэффициент a не может быть равен 0 для квадратного уравнения")
            a = Reader.read_float("a = ")

        return cls(a, b, c)

    def calculate_roots(self):
        """Вычисление корней квадратного уравнения"""
        try:
            discriminant = self.b**2 - 4 * self.a * self.c

            if discriminant > 0:
                # Два различных корня
                x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
                x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
                self.roots = [x1, x2]
            elif discriminant == 0:
                # Один корень (кратности 2)
                x = -self.b / (2 * self.a)
                self.roots = [x]
            else:
                # Действительных корней нет
                self.roots = []

            return self.roots
        except ZeroDivisionError:
            self.roots = []
            return self.roots

    def display(self):
        """Вывод уравнения и его корней"""
        print(f"Уравнение: {self}")

        discriminant = self.b**2 - 4 * self.a * self.c

        if discriminant > 0:
            print(f"Дискриминант: {discriminant:.2f} > 0")
            print(
                f"Два различных корня: x1 = {self.roots[0]:.2f}, x2 = {self.roots[1]:.2f}"
            )
        elif discriminant == 0:
            print(f"Дискриминант: {discriminant:.2f} = 0")
            print(f"Один корень (кратности 2): x = {self.roots[0]:.2f}")
        else:
            print(f"Дискриминант: {discriminant:.2f} < 0")
            print("Действительных корней нет")

    def __str__(self):
        """Строковое представление квадратного уравнения"""
        b_sign = "+" if self.b >= 0 else "-"
        c_sign = "+" if self.c >= 0 else "-"
        b_abs = abs(self.b)
        c_abs = abs(self.c)
        return f"{self.a:.2f}*x^2 {b_sign} {b_abs:.2f}*x {c_sign} {c_abs:.2f} = 0"


def demonstrate_virtual_call(root_obj):
    """Функция, демонстрирующая виртуальный вызов"""
    print("\n" + "=" * 50)
    print("Демонстрация виртуального вызова:")
    print("Тип объекта:", type(root_obj).__name__)
    print("-" * 30)

    # Виртуальный вызов абстрактных методов
    print("Результат str():", str(root_obj))
    print("Корни:", root_obj.calculate_roots())
    print("Вызов display():")
    root_obj.display()
    print("=" * 50)


if __name__ == "__main__":
    print("1. Линейные уравнения:")
    print("-" * 30)

    # Через ввод с клавиатуры
    print("\nСоздадим линейное уравнение через ввод:")
    lin2 = Linear.read_from_keyboard()
    demonstrate_virtual_call(lin2)

    print("\n\n2. Квадратные уравнения:")
    print("-" * 30)

    # Через ввод с клавиатуры
    print("\nСоздадим квадратное уравнение через ввод:")
    sq4 = Square.read_from_keyboard()
    demonstrate_virtual_call(sq4)

    print("\n\n3. Демонстрация полиморфизма (список уравнений):")
    print("-" * 50)

    equations = [
        Linear(4, -8),  # 4x - 8 = 0, корень: 2
        Square(1, -3, 2),  # x^2 - 3x + 2 = 0, корни: 1 и 2
        Linear(-2, 10),  # -2x + 10 = 0, корень: 5
        Square(2, 0, -8),  # 2x^2 - 8 = 0, корни: 2 и -2
        Square(1, 2, 5),  # x^2 + 2x + 5 = 0, корней нет
    ]

    for i, eq in enumerate(equations, 1):
        print(f"\nУравнение {i}:")
        eq.display()
        print(f"Тип: {type(eq).__name__}")
        print("-" * 30)
