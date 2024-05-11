"""Реализация структуры данных, представляющую собой расширенную структуру стек.

[author] - Shershnev.PF

[date] - 07.05.2024
"""

from typing import Union


class ExtendedStack(list):
    """Класс представляющий расширенную структуру стек.

    Эта структура данных поддерживает следующий функционал:
    - добавление элемента на вершину стека (метод append)
    - удаление с вершины стека (метод pop)
    - математические операции:
        - Сложение (метод sum)
        - Вычитание (метод sub)
        - Умножение (метод mul)
        - Целочисленное деление (метод div)
    """

    def sum(self) -> Union[int, float, str]:
        """Операция сложения. Забирает два элемента с вершины стека и возвращает сумму этих элементов на вершину стека."""
        result = self[-1] + self[-2]
        self.pop()
        self.pop()
        self.append(result)
        return result

    def sub(self) -> Union[int, float]:
        """Операция вычитания. Забирает два элемента с вершины стека и возвращает разницу этих элементов на вершину стека."""
        result = self[-1] - self[-2]
        self.pop()
        self.pop()
        self.append(result)
        return result

    def mul(self) -> Union[int, float, str]:
        """Операция умножения. Забирает два элемента с вершины стека и возвращает произведение этих элементов на вершину стека."""
        result = self[-1] * self[-2]
        self.pop()
        self.pop()
        self.append(result)
        return result

    def div(self) -> float:
        """Операция целочисленного делени. Забирает два элемента с вершины стека и возвращает результат целочисленного деления этих элементов на вершину стека."""
        result = self[-1] // self[-2]
        self.pop()
        self.pop()
        self.append(result)
        return result

    def append(self, item):
        """Операция добавления элемента на вершину стека"""
        super().append(item)

    def pop(self):
        """Операция удаление элемента с вершины стека"""
        super().pop()


if __name__ == "__main__":
    qq = ExtendedStack()

    qq.append(1)
    qq.append(2)
    qq.append(3)
    qq.append(4)
    qq.append("abc")
    print(qq)

    qq.mul()

    print(qq)

    qq.pop()
    print(qq)
