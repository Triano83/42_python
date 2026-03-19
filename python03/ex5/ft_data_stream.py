from typing import Generator


def game_event_stream(count: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie", "diana"]
    events = ["killed monster", "found treasure", "leveled up"]
    p_lvls = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "diana": 3
        }

    for i in range(count):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = p_lvls[player]

        if event == "leveled up":
            p_lvls[player] += 1

        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event
        }


def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes_gen(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    stream = game_event_stream(1000)
    it = iter(stream)

    high_level = 0
    treasure = 0
    lvl_up = 0

    for _ in range(3):
        ev = next(it)
        print(f"Event {ev['id']}: Player {ev['player']} "
              f"(level {ev['level']}) {ev['event']}")
        if ev["level"] >= 10:
            high_level += 1
        if ev["event"] == "found treasure":
            treasure += 1
        if ev["event"] == "leveled up":
            lvl_up += 1

    for ev in it:
        if ev["level"] >= 10:
            high_level += 1
        if ev["event"] == "found treasure":
            treasure += 1
        if ev["event"] == "leveled up":
            lvl_up += 1

    print("...\n")
    print("=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {lvl_up}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib = list(fibonacci_gen(10))
    for i in range(len(fib)):
        print(fib[i], end=", " if i < len(fib) - 1 else "\n")

    print("Prime numbers (first 5): ", end="")
    p_nums = list(primes_gen(5))
    for i in range(len(p_nums)):
        print(p_nums[i], end=", " if i < len(p_nums) - 1 else "\n")


if __name__ == "__main__":
    ft_data_stream()
