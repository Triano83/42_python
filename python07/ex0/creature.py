from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, type="Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str):
        super().__init__(name=name, type="Fire/Flying")

    def attack(self):
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str):
        super().__init__(name=name, type="Water")

    def attack(self):
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str):
        super().__init__(name=name, type="Water")

    def attack(self):
        return "Torragon uses Hydro Pump!"
