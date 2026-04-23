from typing import List, Tuple
from ex0.factory import FlameFactory, AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents: List[Tuple[any, any]]) -> None:
    # Creamos las criaturas
    fighters = []
    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    print(f"{len(fighters)} opponents involved\n")
    print("* Battle *\n")

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            c1, s1 = fighters[i]
            c2, s2 = fighters[j]

            print(f"{c1.describe()}")
            print("vs.")
            print(f"{c2.describe()}")
            print("now fight!\n")

            try:
                s1.act(c1)
                s2.act(c2)
            except Exception as e:
                print(e)
            print()


def main() -> None:
    # Tournament 0
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]\n*** Tournament ***")
    battle([(FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]"
          "\n*** Tournament ***")
    battle([(FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
          "\n*** Tournament ***")
    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())])


if __name__ == "__main__":
    main()
