from ex0 import FlameFactory, AquaFactory


def main() -> None:
    fabrica_de_fuego = FlameFactory()
    fabrica_de_agua = AquaFactory()
    flameling = fabrica_de_fuego.create_base()
    pyrodon = fabrica_de_fuego.create_evolved()
    aquabub = fabrica_de_agua.create_base()
    Torragon = fabrica_de_agua.create_evolved()
    print("Testing factory")
    print(f"{flameling.describe()}")
    print(f"{flameling.attack()}")
    print(f"{pyrodon.describe()}")
    print(f"{pyrodon.attack()}")
    print()
    print("Testing factory")
    print(f"{aquabub.describe()}")
    print(f"{aquabub.attack()}")
    print(f"{Torragon.describe()}")
    print(f"{Torragon.attack()}")
    print()
    print("Testing battle")
    print(f"{flameling.describe()}")
    print("vs")
    print(f"{aquabub.describe()}")
    print(" fight!")
    print(f"{flameling.attack()}")
    print(f"{aquabub.attack()}")


if __name__ == "__main__":
    main()
