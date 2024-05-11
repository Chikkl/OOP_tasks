"""Реализация класса Buffer. Необходим для хранения одновременно не более 5-ти элементов, и вывода сумммы этих элементов.

[author] - Shershnev.PF

[date] - 11.05.2024
"""

from typing import List, Union


class Buffer:
    def __init__(self) -> None:
        self.buffer = []
    
    def add(self, *args: Union[int, float]) -> None:
        """Функция для добавления новых элементов в буффер. 

        Если число элементов в буффере превышает 4, то в консоль будет выведенна сумма пятерок (скоплений эллементов по 5 штук), 
        до тех пор пока число элементов в буфере не будет меньше или равно 4.
        """
        self.buffer.extend(args)
        while len(self.buffer) >= 5:
            print(sum(self.buffer[0:5]))
            del self.buffer[0:5]
            

    def get_current_part(self) -> List[Union[int, float]]:
        """Функция для вывода на экран состояния буффера на данный момент.

        Returns:
            List[int, float]: список, содержащий элементы содержащиеся в буфере
        """
        return self.buffer


if __name__ == "__main__":
    buf = Buffer()
    buf.add(1, 2.0, 3)
    print(buf.get_current_part())
    buf.add(4, 5, 6)
    print(buf.get_current_part())
    buf.add(7, 8, 9, 10)
    print(buf.get_current_part())
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    print(buf.get_current_part())
