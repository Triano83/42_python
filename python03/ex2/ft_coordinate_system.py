import math


def ft_coordinate_system() -> None:

    print("=== Game Coordinate System ===")

    position: tuple[int, int, int] = (10, 20, 5)
    origin: tuple[int, int, int] = (0, 0, 0)
    print(f"Position created: {position}")

    x1, y1, z1 = origin
    x2, y2, z2 = position

    distance: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {origin} and {position}: {distance:.2f}\n")

    coord_string: str = "3,4,0"
    print(f'Parsing coordinates: "{coord_string}"')

    try:
        parts: list[str] = coord_string.split(",")
        parsed_position: tuple[int, int, int] = (
            int(parts[0]), int(parts[1]), int(parts[2])
        )
        print(f"Parsed position: {parsed_position}")

        px, py, pz = parsed_position
        dist_parsed: float = math.sqrt(px**2 + py**2 + pz**2)
        print(f"Distance between {origin} and {parsed_position}:"
              f" {dist_parsed}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    invalid_string: str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_string}"')

    try:
        parts = invalid_string.split(",")
        _ = (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    print(f"Player at x={px}, y={py}, z={pz}")
    print(f"Coordinates: X={px}, Y={py}, Z={pz}")


if __name__ == "__main__":
    ft_coordinate_system()
