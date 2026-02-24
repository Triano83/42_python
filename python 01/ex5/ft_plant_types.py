class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_base_info(self):
        return f"{self.name} ({self.__class__.__name__}): {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.get_base_info()}, {self.color} color")
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter + 28 
        print(f"{self.get_base_info()}, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {shade_area} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info(self):
        print(f"{self.get_base_info()}, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")


    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.show_info()
