def main() -> None:
    print("=== Kaboom 1 ===")
    print("")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print("")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    # Esta línea nunca se ejecutará
    res = dark_spell_record("Abra Kadabra", "Arsenic and frogs")
    print(f"Testing record dark spell: {res}")


if __name__ == "__main__":
    main()
