"""Реализация инвентаря игрока и возможности добавления вещей в этот инвентарь. Реализация при помощи функций.

[author] - Shershnev.PF

[date] - 11.05.2024
"""

from typing import Dict, List


def add_to_inventory(inventory: dict, added_items: List[str]) -> Dict[str, int]:
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    
    return inventory

if __name__ == "__main__":
    inv = {'qq': 1, 'no qq':2}
    cool_loot = ['qq', 'no qq', 'no qq', 'qwer']
    inv = add_to_inventory(inv, cool_loot)
    print(inv)