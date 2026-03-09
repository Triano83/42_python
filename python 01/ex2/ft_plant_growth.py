class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow_up(self, days: int) -> None:
        self.height = self.height + (1 * days)

    def age_up(self, days: int) -> None:
        self.age = self.age + (1 * days)


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    days: int = 7

    for plant in plants:
        print("=== Day 1 ===")
        plant.display_info()
        start_height: int = plant.height
        print(f"=== Day {days} ===")
        plant.age_up(days)
        plant.grow_up(days)
        plant.display_info()
        print(f"Growth this week: +{plant.height - start_height}cm")


if __name__ == "__main__":
    main()
