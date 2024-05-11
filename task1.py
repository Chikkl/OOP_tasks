"""Реализация классов котопса и псакота.

[author] - Shershnev.PF

[date] - 07.05.2024
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстрактный класс представляющий животных.
    """
    @abstractmethod
    def say(self, times: int) -> None:
        """Функция вывода производимых животным звуков в консоль, определенное колличество раз.

        Args:
            times (int): Число, сколько раз необходимо повторить звук.
        """
        pass


class Cat(Animal):
    """Класс представляющий кошек.
    """
    def say(self, times: int) -> None:
        """Функция, воспроизведения звуков кошки.

        Args:
            times (int): Число, сколько раз необходимо повторить звук.
        """
        print("Meow " * times)


class Dog(Animal):
    """Класс представляющий собак
    """
    def say(self, times: int) -> None:
        """Функция, воспроизведения звуков собак.

        Args:
            times (int): Число, сколько раз необходимо повторить звук
        """
        print("Bow-Wow " * times)


class CatDog(Cat, Dog):
    pass


class DogCat(Dog, Cat):
    pass

if __name__ == "__main__":
    muteDog = CatDog()
    muteDog.say(3)

    muteCat = DogCat()
    muteCat.say(2)
