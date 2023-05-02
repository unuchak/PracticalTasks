from abc import abstractmethod
from typing import Protocol


class IPocket(Protocol):
    @abstractmethod
    def add_ball(self, count):
        pass

    @abstractmethod
    def get_ball_count(self) -> int:
        pass


class WhitePocket(IPocket):
    def get_ball_count(self):
        return self.balls_count

    def __init__(self, count):
        self.balls_count = count

    def add_ball(self, count):
        self.balls_count += count


class BluePocket(IPocket):

    def __init__(self, count):
        self.balls_count = count

    def add_ball(self, count):
        pass

    def get_ball_count(self) -> int:
        pass


class RedPocket(IPocket):
    def get_ball_count(self) -> int:
        return self.balls_count

    def __init__(self):
        self.balls_count = 0

    def add_ball(self, count):
        self.balls_count += count


if __name__ == "__main__":
    redPocket: IPocket = RedPocket()
    redPocket.add_ball(1)
    redPocket.add_ball(1)
    redPocket.add_ball(1)
    print(redPocket.get_ball_count())
