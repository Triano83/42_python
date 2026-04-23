from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling("Flameling")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon")


class AquaFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub("Aquabub")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon")
