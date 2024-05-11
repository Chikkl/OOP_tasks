"""Реализация инвентаря игрока и возможности добавления вещей в этот инвентарь. Реализация при помощи ООП.

[author] - Shershnev.PF

[date] - 11.05.2024
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Item:
    name: str
    quantity: int


class Inventory:
    """Класс представляющий собой инвентарь."""

    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item):
        """Функция для добавления вещей в инвентарь.

        Args:
            item (Item): вещь, которую необходимо добавить в инвентарь.
        """
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    def get_total_quantity(self, item_name: str) -> int:
        """Фунция для получения колличества определенной вещи в инвентаре.

        Args:
            item_name (str): название вещи, по которому будет производиться поиск.

        Returns:
            int: колличество этой вещи в инвентаре.
        """
        for item in self.items:
            if item.name == item_name:
                return item.quantity
        return 0

    def get_inventory_summary(self) -> Dict[str, int]:
        """Функция для получения всего содержимого инвентаря.

        Returns:
            Dict[str, int]: Словарь со всем содержимым инвентаря.
        """
        summary = {}
        for item in self.items:
            summary[item.name] = item.quantity
        return summary



if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_item(Item("Аптечка", 5))
    inventory.add_item(Item("Аптечка", 3))
    inventory.add_item(Item("Снаряжение", 1))

    print(inventory.get_total_quantity("Аптечка"))

    print(inventory.get_inventory_summary())
