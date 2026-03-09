class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0

        print("=== Garden Security System ===")
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def display_status(self) -> None:
        print(f"Current plant: {self.name} ({self.__height}cm, "
              f"{self.__age} days)")


def main() -> None:
    my_plant: SecurePlant = SecurePlant("Rose", 25, 30)
    print()
    my_plant.set_height(-5)
    print()
    my_plant.display_status()


if __name__ == "__main__":
    main()
