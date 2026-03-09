class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_base_info(self) -> str:
        return (f"{self.name} ({self.__class__.__name__}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.get_base_info()}, {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        shade_area: int = self.trunk_diameter + 28
        print(f"{self.get_base_info()}, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def show_info(self) -> None:
        print(f"{self.get_base_info()}, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===\n")

    rose: Flower = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()

    oak: Tree = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.show_info()


if __name__ == "__main__":
    main()
