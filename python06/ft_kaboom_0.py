import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")

    # Probamos el hechizo de luz
    # Ingredientes permitidos: earth, air, fire, water
    res = alchemy.grimoire.light_spell_record(
        "Fantasy",
        "Earth, wind and fire"
    )

    print(f"Testing record light spell: {res}")


if __name__ == "__main__":
    main()
