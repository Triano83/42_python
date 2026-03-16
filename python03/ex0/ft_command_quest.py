import sys


def ft_command_quest() -> None:
    total: int = len(sys.argv)
    argv_count: int = total - 1

    print("=== Command Quest ===")

    if argv_count == 0:
        print("No arguments provided!")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argv_count}")
        for i in range(1, total):
            print(f"Argument {i}: {sys.argv[i]}")

    if argv_count == 0:
        print(f"Program name: {sys.argv[0]}")

    print(f"Total arguments: {total}")


if __name__ == "__main__":
    ft_command_quest()
