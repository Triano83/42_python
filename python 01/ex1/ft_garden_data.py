class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Registry ===")
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    for plant in garden:
        plant.display_info()


if __name__ == "__main__":
    main()
