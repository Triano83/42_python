from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(f"{creature.attack()}")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Battle error, aborting tournament:"
                            f" Invalid Creature '{creature.name}'"
                            " for this aggressive strategy")

        print(f"{creature.attack()}")
        print(f"{creature.transform()}")

        if "Shiftling" in creature.name:
            print("Shiftling performs a boosted strike!")
        else:
            print("Morphagon unleashes a devastating morph strike!")

        print(f"{creature.revert()}")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Battle error, aborting tournament: "
                            f"Invalid Creature '{creature.name}'"
                            " for this defensive strategy")

        # El orden: Attack -> Heal
        print(f"{creature.attack()}")
        print(f"{creature.heal()}")
