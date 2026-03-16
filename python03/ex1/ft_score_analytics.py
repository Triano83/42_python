import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return

    numbers: list[int] = []

    try:
        for arg in sys.argv[1:]:
            numbers.append(int(arg))
    except ValueError as e:
        print(f"Error: Invalid input found. {e}")
        return

    total_players: int = len(numbers)
    total_score: int = sum(numbers)
    average_score: float = total_score / total_players
    high_score: int = max(numbers)
    low_score: int = min(numbers)
    score_range: int = high_score - low_score

    print(f"Scores processed: {numbers}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
