"""Реализация инвентаря игрока и возможности добавления вещей в этот инвентарь. Реализация при помощи ООП.

[author] - Shershnev.PF

[date] - 11.05.2024
"""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Item:
    name: str
    id: int
    health: int = 0
    attack: int = 0
    defense: int = 0


@dataclass
class Drink:
    id: int
    name: str
    health: int
    attack: int
    defense: int
    price: int


class Inventory:
    """Класс представляющий из себя инвентарь персонажа"""

    def __init__(self) -> None:
        self.items: List[Item] = []
        self.money: int = 100  # Начальное количество денег

    def add_item(self, item: Item) -> None:
        """Функция для добавления новых вещей в инвентарь

        Args:
            item (Item): добавляемая вещь
        """
        self.items.append(item)

    def add_money(self, amount: int) -> None:
        """Функция для добавления денег в кошелек

        Args:
            amount (int): колличество добавляемых денег
        """
        self.money += amount

    def remove_money(self, amount: int) -> None:
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def get_inventory_summary(self) -> Dict[str, int]:
        summary = {}
        for item in self.items:
            summary[item.name] = (item.health, item.attack, item.defense)
        return summary


class Character:
    def __init__(
        self, name: str, base_health: int, base_attack: int, base_defense: int
    ) -> None:
        self.name = name
        self.inventory = Inventory()
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.equipped_items: List[Item] = []
        self._health = base_health

    def equip_item(self, item_id: int) -> None:
        """Функция, для того, чтобы надеть вещи на себя

        Args:
            item_id (int): id вещи из инвентаря
        """
        for i, item in enumerate(self.inventory.items):
            if item.id == item_id:
                self.equipped_items.append(item)
                self.inventory.items.pop(i)
                print(f"Вы надели: {item.name}")
                return
        print("Такой вещи нет в инвентаре.")

    def unequip_item(self, item_id: int) -> None:
        """Функция, чтобы выкинуть вещь из инвентаря.

        Args:
            item_id (int): id вещи из инвентаря
        """
        for i, item in enumerate(self.equipped_items):
            if item.id == item_id:
                self.inventory.items.append(item)
                self.equipped_items.pop(i)
                print(f"Вы выкинули: {item.name}")
                return
        print("Такой вещи нет на вас.")

    @property
    def health(self) -> int:
        return self._health + sum(item.health for item in self.equipped_items)

    @health.setter
    def health(self, value) -> None:
        self._health = value

    @property
    def attack(self) -> int:
        return self.base_attack + sum(item.attack for item in self.equipped_items)

    @property
    def defense(self) -> int:
        return self.base_defense + sum(item.defense for item in self.equipped_items)


class Mob(ABC):
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    @abstractmethod
    def attack(self, character: Character) -> None:
        pass


class Goblin(Mob):
    def attack(self, character: Character) -> None:
        print(f"Гоблин атакует {character.name}!")


class Orc(Mob):
    def attack(self, character: Character) -> None:
        print(f"Орк атакует {character.name}!")


def generate_random_item() -> Item:
    """Функция для генерации предмета со случайными характеристиками

    Returns:
        Item: сгенерированная вещь
    """
    item_names = ["Зелье здоровья", "Меч", "Щит", "Шлем", "Броня"]
    name = random.choice(item_names)
    health = random.randint(0, 10)
    attack = random.randint(0, 5)
    defense = random.randint(0, 5)
    return Item(name, health, attack, defense)


def generate_random_mob() -> Mob:
    """Функция генерации случайных мобов.

    Returns:
        Mob: определенный моб со случайными характеристиками.
    """
    mob_names = ["Гоблин", "Орк"]
    name = random.choice(mob_names)
    health = random.randint(20, 50)
    attack = random.randint(5, 10)
    defense = random.randint(2, 5)
    if name == "Гоблин":
        return Goblin(name, health, attack, defense)
    else:
        return Orc(name, health, attack, defense)


def fight(character: Character, mob: Mob) -> None:
    """Функция отвечающая за реализацию боевой системы между игроком и мобом.

    Args:
        character (Character): объект персонажа, нашего игрока
        mob (Mob): объект моба, которые встречаются в данжах
    """
    while character.health > 0 and mob.health > 0:
        mob.health -= character.attack
        if mob.health <= 0:
            print(f"{character.name} победил {mob.name}!")
            break
        character.health -= mob.attack
        if character.health <= 0:
            print(f"{mob.name} победил {character.name}.")
            break


def display_character_info(character: Character) -> None:
    """Функция отображения характеристик персонажа

    Args:
        character (Character): объект персонажа, информацию о котором мы хотим получить.
    """
    print(f"Имя: {character.name}")
    print(f"Здоровье: {character.health}")
    print(f"Атака: {character.attack}")
    print(f"Защита: {character.defense}")
    print(f"Деньги: {character.inventory.money}")
    #for item, stats in character.inventory.get_inventory_summary().items():
    #    print(f"{item}: Здоровье {stats[0]}, Атака {stats[1]}, Защита {stats[2]}")


def main() -> None:
    """Функция представляющая основной функционал игры. Она отвечает за диалоговые окна отображаемые
    в консоли в ходе игры и обработку входящих от игрока команд.
    """
    character_name = input("Введите имя вашего персонажа: ")
    character = Character(character_name, 100, 10, 5)

    while True:
        print("\nВыберите действие:")
        print("1. Пойти в таверну")
        print("2. Пойти в данж")
        print("3. Проверить инвентарь")
        action = input("Введите номер действия: ")

        if action == "1":
            print("\nДобро пожаловать в таверну!")
            print("Вот наши напитки:")
            drinks = [
                Drink(1, "Зелье лечения", 20, 0, 0, 10),
                Drink(2, "Зелье силы", 0, 5, 0, 15),
                Drink(3, "Зелье защиты", 0, 0, 5, 15),
                Drink(4, "Пиво", 0, -5, 5, 15),
            ]
            for i, drink in enumerate(drinks, start=1):
                print(
                    f"{i}. {drink.name} - Здоровье: {drink.health}, Атака: {drink.attack}, Защита: {drink.defense}, Цена: {drink.price}"
                )
            print(f"Деньги в казне: {character.inventory.money}")
            drink_choice = input("Введите номер напитка, который вы хотите купить: ")
            drink = drinks[int(drink_choice) - 1]
            if character.inventory.remove_money(drink.price):
                character.inventory.add_item(
                    Item(drink.name, drink.health, drink.attack, drink.defense)
                )
                print(f"Вы купили {drink.name}!")
            else:
                print("У вас недостаточно денег для покупки этого напитка.")

        elif action == "2":
            print("\nДобро пожаловать в данж!")
            mob = generate_random_mob()
            print(f"{mob.name} приближается! Его урон {mob.attack}, защита {mob.defense} и здоровье {mob.health}")
            while True:
                print("\nВыберите действие:")
                print("1. Напасть")
                print("2. Убежать")
                action = input("Введите номер действия: ")

                if action == "1":
                    fight(character, mob)
                    if character.health <= 0:
                        print("Игра окончена!")
                        return
                    else:
                        new_item = generate_random_item()
                        character.inventory.add_item(new_item)
                        print(
                            f"Вы победили моба, получили новый предмет '{new_item.name}' и успешно сбежали из данжа."
                        )
                        break
                elif action == "2":
                    if random.random() > 0.5:
                        print("Вы успешно сбежали из данжа.")
                        break
                    else:
                        print("Вам не удалось сбежать.")
                        fight(character, mob)
                        if character.health <= 0:
                            print("Игра окончена!")
                            return

        elif action == "3":
            print("\nХарактеристики персонажа:")
            display_character_info(character)
            print("Инвентарь:")
            for i, item in enumerate(character.inventory.items):
                print(f"{i + 1}. {item.id} - ID: {item}")
            while True:
                print("\nВыберите действие:")
                print("1. Надеть вещь")
                print("2. Выкинуть вещь")
                print("3. Вернуться в меню")
                action = input("Введите номер действия: ")

                if action == "1":
                    item_id = int(input("Введите ID вещи для надевания: "))
                    character.equip_item(item_id)
                elif action == "2":
                    item_id = int(input("Введите ID вещи для выкидывания: "))
                    character.unequip_item(item_id)
                elif action == "3":
                    break
                else:
                    print(
                        "Неверный ввод. Пожалуйста, выберите действие из предложенных."
                    )

        else:
            print("Неверный ввод. Пожалуйста, выберите действие из предложенных.")


if __name__ == "__main__":
    main()
