"""Реализация структуры данных, представляющую собой расширенную структуру стек.

[author] - Shershnev.PF

[date] - 07.05.2024
"""


class Song:
    def __init__(self, artist: str, song_name: str) -> None:
        self.artist = artist
        self.song_name = song_name

    def add_tags(self, *args):
        self.tags = args


if __name__ == "__main__":
    my_song = Song("chikoni", "amg")
    my_song.add_tags("bebra", "foo", "bar")

    print(my_song.__dict__)
