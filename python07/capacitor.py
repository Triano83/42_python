from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability\n")
    h_factory = HealingCreatureFactory()
    sproutling = h_factory.create_base()
    bloomelle = h_factory.create_evolved()

    print("base:")
    print(f"{sproutling.describe()}")
    print(f"{sproutling.attack()}")
    print(f"{sproutling.heal()}\n")

    print("evolved:")
    print(f"{bloomelle.describe()}")
    print(f"{bloomelle.attack()}")
    print(f"{bloomelle.heal()}\n")

    print("Testing Creature with transform capability\n")
    t_factory = TransformCreatureFactory()
    shiftling = t_factory.create_base()
    morphagon = t_factory.create_evolved()

    print("base:")
    print(f"{shiftling.describe()}")
    print(f"{shiftling.attack()}")
    print(f"{shiftling.transform()}")
    print("Shiftling performs a boosted strike!")
    print(f"{shiftling.revert()}\n")

    print("evolved:")
    print(f"{morphagon.describe()}")
    print(f"{morphagon.attack()}")
    print(f"{morphagon.transform()}")
    print("Morphagon unleashes a devastating morph strike!")
    print(f"{morphagon.revert()}")


if __name__ == "__main__":
    main()
