class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
    def display_info(self) -> None:
        print(f"{self.name} ({self.starting_height}cm, {self.starting_age} days)")
def main():
    plants = [
        Plant("Rose",25,30),
        Plant("Sunflower",80,45),
        Plant("Cactus",15,120),
        Plant("Oak",200,365),
        Plant("Fern",15,120)
    ]
    print("=== Plant Factory Output ===")
    i = 0
    for p in plants:
        i = i + 1
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")
    print()
    print(f"Total plants created: {i}")

if __name__ == "__main__":
    main()