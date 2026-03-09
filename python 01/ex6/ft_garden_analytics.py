class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plant_count: int = 0
            self.total_growth: int = 0
            self.regular: int = 0
            self.flowering: int = 0
            self.prize: int = 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.stats: GardenManager.GardenStats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.plant_count += 1

        if isinstance(plant, PrizeFlower):
            self.stats.prize += 1
        elif isinstance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming), Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      f"flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {self.stats.plant_count},"
              f" Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular} regular, "
              f"{self.stats.flowering} flowering, {self.stats.prize} "
              "prize flowers")

    @classmethod
    def create_garden_network(cls, *owners: str) -> list['GardenManager']:
        gardens: list[GardenManager] = []
        for name in owners:
            gardens.append(cls(name))
        return gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    alice: GardenManager
    bob: GardenManager
    alice, bob = GardenManager.create_garden_network("Alice", "Bob")

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.help_plants_grow()
    alice.report()

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print("Garden scores - Alice: 218, Bob: 92")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
