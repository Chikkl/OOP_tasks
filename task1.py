"""Реализация классов котопса и псакота

[author] - Shershnev.PF

[date] - 07.05.2024
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say(self, times: int) -> None:
        pass


class Cat(Animal):
    def say(self, times: int) -> None:
        print("Meow " * times)


class Dog(Animal):
    def say(self, times: int) -> None:
        print("Bow-Wow " * times)


class CatDog(Cat, Dog):
    pass


class DogCat(Dog, Cat):
    pass


muteDog = CatDog()
muteDog.say(3)

muteCat = DogCat()
muteCat.say(2)
