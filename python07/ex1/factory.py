from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creature import Sproutling, Bloomelle, Morphagon, Shiftling


class HealingCreatureFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Sproutling("Sproutling")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle")


class TransformCreatureFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self) -> Creature:
        return Shiftling("Shiftling")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon")
