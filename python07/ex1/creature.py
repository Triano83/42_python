from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name=name, type="Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name=name, type="Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str):
        super().__init__(name=name, type="Normal")

    def attack(self) -> str:
        return "Shiftling attacks normally."

    def transform(self) -> str:
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str):
        super().__init__(name=name, type="Normal/Dragon")

    def attack(self) -> str:
        return "Morphagon attacks normally."

    def transform(self) -> str:
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."
