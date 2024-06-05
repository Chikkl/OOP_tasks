"""Реализация инвентаря игрока и возможности добавления вещей в этот инвентарь. Реализация при помощи ООП.

[author] - Shershnev.PF

[date] - 11.05.2024
"""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Literal, Self


@dataclass
class Item:
    """Датакласс вещи"""

    id: int
    name: str
    health: int = 0
    attack: int = 0
    defense: int = 0


@dataclass
class Drink:
    """Датакласс напитка"""

    id: int
    name: str
    health: int
    attack: int
    defense: int
    price: int


class Inventory:
    """Класс представляющий из себя инвентарь персонажа"""

    def __init__(self: Self) -> None:
        self.items: List[Item] = []
        self.money: int = 100  # Начальное количество денег

    def add_item(self: Self, item: Item) -> None:
        """Функция для добавления новых вещей в инвентарь

        Args:
            item (Item): добавляемая вещь
        """
        self.items.append(item)

    def add_money(self: Self, amount: int) -> None:
        """Функция для добавления денег в кошелек

        Args:
            amount (int): колличество добавляемых денег
        """
        self.money += amount

    def remove_money(self: Self, amount: int) -> bool:
        """Функция для убавления денег из кошелька.

        Args:
            amount (int): кол-во отнимаемых денег.

        Returns:
            bool: Успешность выполнения операции.
        """
        if self.money >= amount:
            self.money -= amount
            return True
        return False

    def get_inventory_summary(self: Self) -> Dict[str, int]:
        """Функция отображения инвентаря

        Returns:
            Dict[str, int]: словарь, содержащий в себе информацию о вещах из инвентаря.
        """
        summary = {}
        for item in self.items:
            summary[item.name] = (item.health, item.attack, item.defense)
        return summary


class Character:
    def __init__(
        self: Self, name: str, base_health: int, base_attack: int, base_defense: int
    ) -> None:
        self.name = name
        self.inventory = Inventory()
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.equipped_items: List[Item] = []
        self._health = base_health

    def equip_item(self: Self, item_id: int) -> None:
        """Функция, для того, чтобы надеть вещи на себя

        Args:
            item_id (int): id вещи из инвентаря
        """
        for i, item in enumerate(self.inventory.items):
            if item.id == item_id:
                self.equipped_items.append(item)
                self.inventory.items.pop(i)
                print(f"Вы надели: {item.name}")
        print("Такой вещи нет в инвентаре.")

    def unequip_item(self: Self, item_id: int) -> None:
        """Функция, чтобы выкинуть вещь из инвентаря.

        Args:
            item_id (int): id вещи из инвентаря
        """
        for i, item in enumerate(self.equipped_items):
            if item.id == item_id:
                self.inventory.items.append(item)
                self.equipped_items.pop(i)
                print(f"Вы выкинули: {item.name}")
        print("Такой вещи нет на вас.")

    @property
    def health(self: Self) -> int:
        """Геттер здоровья."""
        return self._health + sum(item.health for item in self.equipped_items)

    @health.setter
    def health(self: Self, value: int) -> None:
        """Сеттер здоровья."""
        self._health = value

    @property
    def attack(self: Self) -> int:
        """Геттер здлоровья."""
        return self.base_attack + sum(item.attack for item in self.equipped_items)

    @property
    def defense(self: Self) -> int:
        """Сеттер здоровья."""
        return self.base_defense + sum(item.defense for item in self.equipped_items)


class Mob(ABC):
    """Абстрактный класс, для дальнейшей генерации различных мобов."""

    def __init__(self: Self, name: str, health: int, attack: int, defense: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Goblin(Mob):
    def attack(self: Self, character: Character) -> None:
        print(f"Гоблин атакует {character.name}!")


class Orc(Mob):
    def attack(self: Self, character: Character) -> None:
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


class DifficultyStrategy(ABC):
    @abstractmethod
    def generate_items(self: Self):
        """Функция генерация вещей."""
        pass

    @abstractmethod
    def generate_mobs(self: Self):
        """Функция генерация врагов."""
        pass


class EasyDifficulty(DifficultyStrategy):
    def generate_items(self: Self) -> Item:
        """Функция генерация вещей."""
        easy_items = [
            Item(1, "Меч из обычного дерева", 0, 5, 0),
            Item(2, "Кольчуга", 0, 0, 3),
            Item(3, "Зелье лечения", 10, 0, 0),
        ]
        return random.sample(easy_items, random.randint(1, len(easy_items)))

    def generate_mobs(self: Self) -> Item:
        """Функция генерация врагов."""
        easy_mobs = [
            Mob("Гоблин", 20, 5, 2),
            Mob("Крыса", 5, 1, 0),
        ]
        return random.sample(easy_mobs, random.randint(1, len(easy_mobs)))


class MiddleDifficulty(DifficultyStrategy):
    def generate_items(self: Self) -> Item:
        """Функция генерация вещей."""
        middle_items = [
            Item(4, "Меч из закальеванной стали", 0, 10, 0),
            Item(5, "Латный щит", 0, 0, 5),
            Item(6, "Зелье силы", 0, 10, 0),
        ]
        return random.sample(middle_items, random.randint(1, len(middle_items)))

    def generate_mobs(self: Self) -> Item:
        """Функция генерация врагов."""
        middle_mobs = [
            Mob("Орк", 30, 8, 3),
            Mob("Гном", 15, 3, 1),
        ]
        return random.sample(middle_mobs, random.randint(1, len(middle_mobs)))


class HardDifficulty(DifficultyStrategy):
    def generate_items(self: Self) -> Item:
        """Функция генерация вещей."""
        hard_items = [
            Item(7, "Меч из черного железа", 0, 15, 0),
            Item(8, "Алмазная броня", 0, 0, 10),
            Item(9, "Зелье защиты", 0, 0, 10),
        ]
        return random.sample(hard_items, random.randint(1, len(hard_items)))

    def generate_mobs(self: Self) -> Item:
        """Функция генерация врагов."""
        hard_mobs = [
            Mob("Тролль", 40, 10, 4),
            Mob("Дракон", 50, 15, 5),
        ]
        return random.sample(hard_mobs, random.randint(1, len(hard_mobs)))


class Game:
    """Класс игры, для генерации мобов, вещей и установки определенной сложности."""

    def __init__(self):
        self.items = []
        self.mobs = []
        self.difficulty_strategy = None

    def set_difficulty(self: Self, difficulty: Literal["easy", "middle", "hard"]):
        """Функция для установки определенной сложности

        Args:
            difficulty (Literal["easy", "middle", "hard"]): сложность игры

        Raises:
            ValueError: ошибка вызываемая, если нет введённой сложности
        """
        if difficulty == "easy":
            self.difficulty_strategy = EasyDifficulty()
        elif difficulty == "middle":
            self.difficulty_strategy = MiddleDifficulty()
        elif difficulty == "hard":
            self.difficulty_strategy = HardDifficulty()
        else:
            raise ValueError("Invalid difficulty level")

    def generate_world(self: Self):
        """Генерация мира, а именно вещей и вражеских мобов.

        Raises:
            ValueError: ошибка вызываемая, если игрок ввёл несуществующую сложность
        """
        if self.difficulty_strategy:
            self.items = self.difficulty_strategy.generate_items()
            self.mobs = self.difficulty_strategy.generate_mobs()
        else:
            raise ValueError("Difficulty strategy is not set")


class Action(ABC):
    """Абстрактный класс, представляющий из себя некоторое действие."""

    def __init__(self: Self, character: Character, game: Game) -> None:
        self.character = character
        self.game = game

    @abstractmethod
    def execute(self: Self):
        raise NotImplementedError("Метод execute должен быть реализован в подклассе")


class GoToTavern(Action):
    """Класс действия для похода в таверну"""

    def __init__(self: Self, character: Character, game: Game) -> None:
        super().__init__(character, game)
        self.name = "Пойти в таверну"

    def execute(self: Self) -> Character:
        """Функция ыполнение действия"""
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
        print(f"Деньги в казне: {self.character.inventory.money}")
        drink_choice = input("Введите номер напитка, который вы хотите купить: ")
        drink = drinks[int(drink_choice) - 1]
        if self.character.inventory.remove_money(drink.price):
            self.character.inventory.add_item(
                Item(drink.name, drink.health, drink.attack, drink.defense)
            )
            print(f"Вы купили {drink.name}!")
        else:
            print("У вас недостаточно денег для покупки этого напитка.")
        return self.character


class GoToDungeon(Action):
    """Действие поход в данж, содержит в себе функцию выполнения этого действия, систему боёвки и наград."""

    def __init__(self: Self, character: Character, game: Game) -> None:
        super().__init__(character, game)
        self.name = "Пойти в данж"

    def execute(self: Self) -> Character:
        """Функция для выполнения действия"""
        print("\nДобро пожаловать в данж!")
        mob = random.choice(self.game.mobs)
        print(
            f"{mob.name} приближается! Его урон {mob.attack}, защита {mob.defense} и здоровье {mob.health}"
        )
        while True:
            print("\nВыберите действие:")
            print("1. Напасть")
            print("2. Убежать")
            action = input("Введите номер действия: ")

            if action == "1":
                fight(self.character, mob)
                if self.character.health <= 0:
                    print("Игра окончена!")
                    break
                else:
                    new_item = random.choice(self.game.items)
                    self.character.inventory.add_item(new_item)
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
                    fight(self.character, mob)
                    if self.character.health <= 0:
                        print("Игра окончена!")
                        break
        return self.character


class CheckInventory(Action):
    """Действие для проверки инвентаря и характеристик персонажа"""

    def __init__(self: Self, character: Character, game: Game) -> None:
        super().__init__(character, game)
        self.name = "Посмотреть инвентарь"

    def execute(self: Self) -> Character:
        """Функция для выполнения действия"""

        print("\nХарактеристики персонажа:")
        display_character_info(self.character)
        print("Инвентарь:")
        for i, item in enumerate(self.character.inventory.items):
            print(f"{i + 1}. {item.id} - ID: {item}")
        while True:
            print("\nВыберите действие:")
            print("1. Надеть вещь")
            print("2. Выкинуть вещь")
            print("3. Вернуться в меню")
            action = input("Введите номер действия: ")

            if action == "1":
                item_id = int(input("Введите ID вещи для надевания: "))
                self.character.equip_item(item_id)
            elif action == "2":
                item_id = int(input("Введите ID вещи для выкидывания: "))
                self.character.unequip_item(item_id)
            elif action == "3":
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите действие из предложенных.")
        return self.character


def main(actions: Dict[str, Action]) -> None:
    """Функция представляющая основной функционал игры. Она отвечает за диалоговые окна отображаемые
    в консоли в ходе игры и обработку входящих от игрока команд.

    Args:
        actions (Dict[str, Action]): словарь с действиями, которые может выполнять игрок в главном меню.
    """

    game = Game()
    difficulty = input("Выберите уровень сложности (easy/middle/hard): ")
    game.set_difficulty(difficulty)
    game.generate_world()

    character_name = input("Введите имя вашего персонажа: ")
    character = Character(character_name, 100, 10, 5)

    while True:
        print("\nВыберите действие:")
        for number, action in actions.items():
            print(f"{number}. {action(character, game).name}")

        action_choice = input("Введите номер действия: ")
        action = actions.get(action_choice)

        if action:
            character = action(character, game).execute()
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из предложенных.")


if __name__ == "__main__":
    actions = {
        "1": GoToTavern,
        "2": GoToDungeon,
        "3": CheckInventory,
    }
    main(actions)
