def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        "first_kill", "level_10", "treasure_hunter", "speed_demon"
    }
    bob: set[str] = {
        "first_kill", "level_10", "boss_slayer", "collector"
    }
    charlie: set[str] = {
        "level_10", "treasure_hunter", "boss_slayer",
        "speed_demon", "perfectionist"
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements: set[str] = alice.union(bob, charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common: set[str] = alice.intersection(bob, charlie)

    only_alice: set[str] = alice.difference(bob, charlie)
    only_bob: set[str] = bob.difference(alice, charlie)
    only_charlie: set[str] = charlie.difference(alice, bob)
    rare: set[str] = only_alice.union(only_bob, only_charlie)

    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}\n")

    alice_bob_common: set[str] = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_only: set[str] = alice.difference(bob)
    print(f"Alice unique: {alice_only}")

    bob_only: set[str] = bob.difference(alice)
    print(f"Bob unique: {bob_only}")


if __name__ == "__main__":
    ft_achievement_tracker()
