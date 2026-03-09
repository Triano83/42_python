class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_info(self) -> None:
        print(f"{self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Oak", 200, 365),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plant_count: int = 0
    for p in plants:
        plant_count = plant_count + 1
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")

    print()
    print(f"Total plants created: {plant_count}")


if __name__ == "__main__":
    main()
